from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model

from src.rewards.models import RewardLog

User = get_user_model()

@shared_task
def process_scheduled_reward(reward_id):
    from src.rewards.models import ScheduledReward  # избежать циклического импорта
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
        if reward.execute_at <= timezone.now():
            user = reward.user
            user.coins += reward.amount 
            user.save()

            RewardLog.objects.create(user=user, amount=reward.amount)

    except ScheduledReward.DoesNotExist:
        ...
