from django.apps import AppConfig


class SAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 's_app'

    def ready(self):
        import s_app.signals  # Import signals on app startup
