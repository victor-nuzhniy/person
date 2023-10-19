"""Factories for testing 'service' app."""
import factory

from api.models import Team, User
from tests.bases import BaseModelFactory


class TeamFactory(BaseModelFactory):
    """Factory for testing Team model."""

    class Meta:
        """Class Meta for TeamFactory."""

        model = Team
        exclude = ("user_set",)

    name: str = factory.Faker("pystr", min_chars=1, max_chars=50)
    user_set = factory.RelatedFactoryList(
        factory="tests.api.factories.UserFactory",
        factory_related_name="user_set",
        size=0,
    )


class UserFactory(BaseModelFactory):
    """Factory for testing User model."""

    class Meta:
        """Class Meta for UserFactory."""

        model = User
        django_get_or_create = ("team",)

    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_staff = factory.Faker("pybool")
    is_active = factory.Faker("pybool")
    date_joined = factory.Faker("date_time")
    password = factory.Faker("pystr", min_chars=1, max_chars=128)
    last_login = factory.Faker("date_time")
    team = factory.SubFactory(TeamFactory)
