from django.apps import AppConfig



class MessdeckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messdeck'

    def ready(self):
        import messdeck.signals