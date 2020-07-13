from django.apps import AppConfig


class CommentsConfig(AppConfig):
    name = "apps.comments"

    def ready(self):
        from . import signals  # noqa
