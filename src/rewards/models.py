from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    execute_at = models.DateTimeField()

class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} + {self.amount} = {self.user.coins}'
