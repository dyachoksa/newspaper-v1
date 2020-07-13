from django.conf import settings
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="author",
        on_delete=models.CASCADE,
        related_name="posted_comments",
    )
    article = models.ForeignKey(
        "articles.Article",
        verbose_name="article",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField(verbose_name="content")
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    def __str__(self):
        return f"Comment on Article#{self.article_id}"

    def __repr__(self):
        return "<Comment id={} user_id={} article_id={}>".format(
            self.pk, self.user_id, self.article_id
        )
