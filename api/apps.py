"""App configurations for api app."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """App configurations for api app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
