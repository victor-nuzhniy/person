"""Class and function views for api app."""
from django.db.models import QuerySet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.schemas import AutoSchema
from rest_framework.serializers import Serializer

from api.models import Team, User
from api.schemas import (
    swagger_team_schema,
    swagger_user_register_schema,
    swagger_user_responses,
)
from api.serializers import CreateUserSerializer, TeamSerializer, UserSerializer


class RegisterView(CreateModelMixin, GenericAPIView):
    """Class view for user registering."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = CreateUserSerializer

    @swagger_auto_schema(
        request_body=swagger_user_register_schema,
        responses=swagger_user_responses,
    )
    def post(self, request, *args, **kwargs):
        """Create user."""
        return self.create(request, *args, **kwargs)


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

    @swagger_auto_schema(responses=swagger_user_responses)
    def get(self, request, *args, **kwargs):
        """Get user by pk."""
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=swagger_user_register_schema,
        responses=swagger_user_responses,
    )
    def put(self, request, *args, **kwargs):
        """Update user by pk."""
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=swagger_user_register_schema,
        responses=swagger_user_responses,
    )
    def patch(self, request, *args, **kwargs):
        """Update partially by pk."""
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(responses=swagger_user_responses)
    def delete(self, request, *args, **kwargs):
        """Delete user by pk."""
        return self.destroy(request, *args, **kwargs)


class UsersView(ListModelMixin, GenericAPIView):
    """Class view for list user."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = UserSerializer
    queryset: QuerySet = User.objects.all()

    @swagger_auto_schema(responses=swagger_user_responses)
    def get(self, request, *args, **kwargs):
        """Retrieve users list."""
        return self.list(request, *args, **kwargs)


class TeamView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    """Class view for team retrieve, update and delete."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = TeamSerializer
    queryset: QuerySet = Team.objects.all()

    @swagger_auto_schema(responses=swagger_user_responses)
    def get(self, request, *args, **kwargs):
        """Get team by pk."""
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=swagger_team_schema,
        responses=swagger_user_responses,
    )
    def put(self, request, *args, **kwargs):
        """Update team by pk."""
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(responses=swagger_user_responses)
    def delete(self, request, *args, **kwargs):
        """Delete team by pk."""
        return self.destroy(request, *args, **kwargs)


class TeamsView(CreateModelMixin, ListModelMixin, GenericAPIView):
    """Class view for creating and get many teams."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = TeamSerializer
    queryset: QuerySet = Team.objects.all()

    @swagger_auto_schema(responses=swagger_user_responses)
    def get(self, request, *args, **kwargs):
        """Retrieve teams list."""
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=swagger_team_schema,
        responses=swagger_user_responses,
    )
    def post(self, request, *args, **kwargs):
        """Create team."""
        return self.create(request, *args, **kwargs)
