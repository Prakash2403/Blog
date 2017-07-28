import os

from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'post'

    if os.environ.get('ELASTICSEARCH_ENABLED', True):
        def ready(self):
            import utils.signals
