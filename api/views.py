"""Class and function views for api app."""

from rest_framework.generics import CreateAPIView
from rest_framework.schemas import AutoSchema
from rest_framework.serializers import Serializer

from api.serializers import UserSerializer


class RegisterView(CreateAPIView):
    """Class view for user registering."""

    schema: AutoSchema = AutoSchema()
    serializer_class: Serializer = UserSerializer
