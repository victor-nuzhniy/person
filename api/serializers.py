"""Module for api app serializers."""
from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    """User model serializer class."""

    class Meta:
        """Class Meta for User serializer class."""

        model = User
        fields = ["id", "email", "first_name", "last_name", "password", "team"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Create user with validated_data."""
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
