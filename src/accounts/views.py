from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import permissions


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class RefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

class VerifyTokenView(TokenVerifyView):
    permission_classes = [permissions.AllowAny]