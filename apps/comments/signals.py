from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.articles.models import Article

from .models import Comment


@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance: Comment, created: bool, **kwargs):
    if not created:
        return

    Article.objects.filter(pk=instance.article_id).update(
        comments_count=F("comments_count") + 1
    )


@receiver(post_delete, sender=Comment)
def comment_post_delete(sender, instance: Comment, **kwargs):
    Article.objects.filter(pk=instance.article_id).update(
        comments_count=F("comments_count") - 1
    )
