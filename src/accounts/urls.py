from django.urls import path

from src.accounts.views import LoginView, RefreshView, VerifyTokenView 

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('refresh/', RefreshView.as_view(), name='refresh-token'),
    path('verify/', VerifyTokenView.as_view(), name='verify-token'),
]