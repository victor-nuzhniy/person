"""Common functionality for api app."""
from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnly(BasePermission):
    """Custom permission 'readonly'."""

    def has_permission(self, request, view):
        """State that method in safe methods list."""
        return request.method in SAFE_METHODS
