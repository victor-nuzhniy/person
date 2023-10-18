"""Class and function views for api app."""
from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.schemas import AutoSchema
from rest_framework.serializers import Serializer

from api.models import User
from api.serializers import CreateUserSerializer, UserSerializer


class RegisterView(CreateAPIView):
    """Class view for user registering."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = CreateUserSerializer


class UserView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    """Class view for user retrieve, update and delete."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = UserSerializer
    queryset: QuerySet = User.objects.all()

    def get(self, request, *args, **kwargs):
        """Get user by pk."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update user by pk."""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Update partially by pk."""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete user by pk."""
        return self.destroy(request, *args, **kwargs)


class UsersView(ListAPIView):
    """Class view for list user."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = UserSerializer
    queryset: QuerySet = User.objects.all()
