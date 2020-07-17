from django.contrib import admin
from django.contrib.auth import get_user_model
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Category


User = get_user_model()


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
        "author",
        "is_published",
        "is_featured",
        "comments_count",
        "published_at",
        "created_at",
    )
    list_display_links = ("pk", "title")
    list_filter = ("is_published", "is_featured", "is_category_featured")
    list_select_related = ("category", "author")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(staff_profile__pk__isnull=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ("name",)

    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ("created_at", "updated_at")

    list_display = ("pk", "name", "created_at", "updated_at")
    list_display_links = ("pk", "name")
