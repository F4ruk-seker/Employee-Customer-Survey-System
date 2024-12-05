from django.apps import AppConfig


class AnketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anket'

    def ready(self):
        import anket.signals

