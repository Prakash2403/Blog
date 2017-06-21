import os

from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'post'

    if os.environ.get('ELASTICSEARCH_ENABLED', False):
        def ready(self):
            import signals