from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    readonly_fields = ("user", "article", "content", "created_at", "updated_at")

    list_display = ("pk", "user", "article", "created_at", "updated_at")
    list_display_links = ("pk", "user", "article")
    list_select_related = ("user", "article")
