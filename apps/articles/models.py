from django.db import models


class Article(models.Model):
    title = models.CharField(
        verbose_name="title", max_length=150, blank=False, null=False
    )
    slug = models.SlugField(
        max_length=160, blank=True, null=False, unique_for_date="published_at"
    )
    description = models.TextField(verbose_name="description", max_length=600)
    content = models.TextField(verbose_name="content")
    is_published = models.BooleanField(
        verbose_name="is published", blank=True, default=False
    )
    published_at = models.DateTimeField(
        verbose_name="published at", blank=True, null=True, default=None
    )
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

        indexes = (
            models.Index(fields=("-created_at",)),
            models.Index(fields=("is_published", "-published_at")),
            models.Index(fields=("slug", "published_at")),
        )

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Article id={} title={} is_published={}>".format(
            self.pk, self.title, self.is_published
        )
