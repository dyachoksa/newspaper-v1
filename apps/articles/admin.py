from django.contrib import admin

from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    ordering = ("-created_at",)

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ("created_at", "updated_at")

    search_fields = ("title",)

    list_display = ("pk", "title", "is_published", "published_at", "created_at")
    list_display_links = ("pk", "title")
    list_filter = ("is_published",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ("name",)

    prepopulated_fields = {"slug": ("name",)}

    list_display = ("pk", "name", "created_at")
    list_display_links = ("pk", "name")
