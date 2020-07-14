from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_at"

    ordering = ("-created_at",)

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ("created_at", "updated_at", "comments_count")

    search_fields = ("title",)
    summernote_fields = ("content",)

    list_display = (
        "pk",
        "title",
        "category",
        "is_published",
        "is_featured",
        "comments_count",
        "published_at",
        "created_at",
    )
    list_display_links = ("pk", "title")
    list_filter = ("is_published", "is_featured", "is_category_featured")
    list_select_related = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ("name",)

    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ("created_at", "updated_at")

    list_display = ("pk", "name", "created_at", "updated_at")
    list_display_links = ("pk", "name")
