import os
import uuid

from django.utils import timezone


def article_image_upload_to(instance, filename):
    today = timezone.now()

    basedir = today.strftime("articles/covers/%Y/%m")
    extension = os.path.splitext(filename)[1]
    name = uuid.uuid4()

    return f"{basedir}/{name}{extension}"
