from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Article


@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance: Article, **kwargs):
    if instance.is_published and instance.published_at is None:
        instance.published_at = timezone.now()
