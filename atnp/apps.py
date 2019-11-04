from django.apps import AppConfig


class AtnpConfig(AppConfig):
    name = 'atnp'

    def ready(self):
        import notification.signals  # noqa
