from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pars_auth'
    # verbose_name = 'Pars Auth'

    def ready(self):
        import pars_auth.signals


