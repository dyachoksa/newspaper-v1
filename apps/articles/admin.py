from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ("created_at", "updated_at")

    search_fields = ("title",)

    list_display = ("pk", "title", "is_published", "published_at", "created_at")
    list_display_links = ("pk", "title")
    list_filter = ("is_published",)
