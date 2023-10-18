"""Admin site settings for api app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Team, User


class CustomUserAdmin(UserAdmin):
    """Customized UserAdmin class with additional fields."""

    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "team",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )


class TeamAdmin(admin.ModelAdmin):
    """Team admin site configuration."""

    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(User, CustomUserAdmin)
admin.site.register(Team, TeamAdmin)
