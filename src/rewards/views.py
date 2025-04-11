from datetime import timedelta

from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.rewards.models import RewardLog, ScheduledReward

class RewardListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user).order_by('-given_at')

    def list(self, request):
        queryset = self.get_queryset()
        return Response([
            {"amount": r.amount, "given_at": r.given_at} for r in queryset
        ])

class RewardRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        today = timezone.now().date()

        if RewardLog.objects.filter(user=user, given_at__date=today).exists():
            return Response({"detail": "You already claimed your reward today."},
                            status=status.HTTP_400_BAD_REQUEST)

        execute_at = timezone.now() + timedelta(minutes=5)
        ScheduledReward.objects.create(user=user, amount=1, execute_at=execute_at)

        return Response({"detail": "Reward scheduled."})
