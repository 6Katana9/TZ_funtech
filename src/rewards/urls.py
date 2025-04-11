from django.urls import path
from src.rewards.views import RewardListView, RewardRequestView


urlpatterns = [
    path('', RewardListView.as_view()),
    path('request/', RewardRequestView.as_view()),
]