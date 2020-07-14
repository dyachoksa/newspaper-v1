from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize, Thumbnail

from .storage import article_image_upload_to


class PublishedArticlesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


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

    def get_absolute_url(self):
        return reverse("articles:by_category", args=(self.slug,))


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
    image = models.ImageField(
        verbose_name="image",
        help_text="Article main image",
        blank=True,
        null=True,
        max_length=150,
        upload_to=article_image_upload_to,
    )
    description = models.TextField(verbose_name="description", max_length=600)
    content = models.TextField(verbose_name="content")
    is_featured = models.BooleanField(
        verbose_name="is featured",
        default=False,
        blank=True,
        help_text="Mark an article as a featured on home page",
    )
    is_category_featured = models.BooleanField(
        verbose_name="is category featured", default=False, blank=True
    )
    is_published = models.BooleanField(
        verbose_name="is published", blank=True, default=False
    )
    published_at = models.DateTimeField(
        verbose_name="published at", blank=True, null=True, default=None
    )
    comments_count = models.IntegerField(
        verbose_name="number of comments",
        blank=False,
        null=False,
        default=0,
        help_text=(
            "Number of comments associated with this article. "
            "Calculates automatically after posting each comment."
        ),
    )
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    objects = models.Manager()
    published = PublishedArticlesManager()

    image_100x100 = ImageSpecField(
        source="image", processors=[Thumbnail(100, 100, anchor="auto")], format="PNG"
    )
    image_730x350 = ImageSpecField(
        source="image",
        processors=[SmartResize(730, 350)],
        format="JPEG",
        options={"quality": 90},
    )
    image_420x330 = ImageSpecField(
        source="image",
        processors=[SmartResize(420, 330)],
        format="JPEG",
        options={"quality": 90},
    )

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

        indexes = (
            models.Index(fields=("-comments_count",)),
            models.Index(fields=("-created_at",)),
            models.Index(fields=("is_category_featured",)),
            models.Index(fields=("is_published", "-published_at")),
            models.Index(fields=("slug", "published_at")),
        )

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Article id={} title={} is_published={}>".format(
            self.pk, self.title, self.is_published
        )
