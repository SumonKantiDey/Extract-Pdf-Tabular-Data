from django.apps import AppConfig


class TextExtractionConfig(AppConfig):
    name = 'text_extraction'

    def ready(self):
        from data_update import updater
        updater.start()
