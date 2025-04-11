from django.urls import path

from src.users.views import UserGetMeView 

urlpatterns = [
    path('', UserGetMeView.as_view(), name='get_me'),
]