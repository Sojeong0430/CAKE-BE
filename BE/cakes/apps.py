from django.apps import AppConfig

class Cake_CustomConfig(AppConfig):
    name = 'cakes'

    def ready(self):
        import cakes.signals