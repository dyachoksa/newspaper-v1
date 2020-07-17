from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from .storage import staff_photo_upload_to


class StaffProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="staff_profile"
    )
    position = models.CharField(
        verbose_name="position title", max_length=250, default="Author"
    )
    photo = models.ImageField(
        verbose_name="photo", upload_to=staff_photo_upload_to, blank=True, null=True
    )
    bio = models.TextField(
        verbose_name="biography",
        blank=True,
        null=True,
        help_text="Optional author biography or other short personal information",
    )
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    photo_400x400 = ImageSpecField(
        source="photo", processors=[SmartResize(400, 400)], format="PNG",
    )

    class Meta:
        verbose_name = "staff profile"
        verbose_name_plural = "staff profiles"

    def __str__(self):
        return self.position

    def __repr__(self):
        return "<StaffProfile id={} user_id={} position={}>".format(
            self.pk, self.user_id, self.position
        )
