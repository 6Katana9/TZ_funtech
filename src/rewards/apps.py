from django.apps import AppConfig


class RewardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.rewards'

    def ready(self):
        import src.rewards.signals