from django.shortcuts import render
from rest_framework import permissions, generics

from src.users.serializers import UserSerializer


class UserGetMeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user