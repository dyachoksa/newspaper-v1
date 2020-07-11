from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Category id={} name={}>".format(self.pk, self.name)


class Article(models.Model):
    title = models.CharField(
        verbose_name="title", max_length=150, blank=False, null=False
    )
    slug = models.SlugField(
        max_length=160, blank=True, null=False, unique_for_date="published_at"
    )
    category = models.ForeignKey(
        Category,
        verbose_name="category",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
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
