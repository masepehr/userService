from django.apps import AppConfig


class UserserviceConfig(AppConfig):
    name = 'UserService'

    def ready(self):
        import UserService.receivers
