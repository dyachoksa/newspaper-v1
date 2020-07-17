from django.contrib import admin

from .models import StaffProfile


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

    list_display = (
        "id",
        "position",
        "user",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "position")
    list_filter = ("created_at",)
    list_select_related = ("user",)
