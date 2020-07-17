import os
import uuid

from django.utils import timezone


def staff_photo_upload_to(instance, filename):
    today = timezone.now()

    basedir = today.strftime("users/photos/%Y")
    extension = os.path.splitext(filename)[1]
    name = uuid.uuid4()

    return f"{basedir}/{name}{extension}"
