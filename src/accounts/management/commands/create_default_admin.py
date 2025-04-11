from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from decouple import config

DEFAULT_ADMIN_USERNAME = config("DEFAULT_ADMIN_USERNAME")
DEFAULT_ADMIN_PASSWORD = config("DEFAULT_ADMIN_PASSWORD")



class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        if not user.objects.filter(username=DEFAULT_ADMIN_USERNAME).first():
            get_user_model().objects.create_superuser(
                username=DEFAULT_ADMIN_USERNAME,
                password=DEFAULT_ADMIN_PASSWORD,
            )