"""Module for testing 'api' app tables."""
import pytest

from api.models import Team, User
from tests.api.factories import TeamFactory, UserFactory
from tests.bases import BaseModelFactory


@pytest.mark.django_db
class TestUser:
    """Class for testing User model."""

    pytestmark = pytest.mark.django_db

    def test_factory(self) -> None:
        """Test User model instance creation."""
        BaseModelFactory.check_factory(factory_class=UserFactory, model=User)

    def test__str__(self) -> None:
        """Test User __str__ method."""
        obj: User = UserFactory()
        expected_result = str(obj.email)
        assert expected_result == obj.__str__()


@pytest.mark.django_db
class TestTeam:
    """Class for testing Team model."""

    pytestmark = pytest.mark.django_db

    def test_factory(self) -> None:
        """Test User model instance creation."""
        BaseModelFactory.check_factory(factory_class=TeamFactory, model=Team)

    def test__str__(self) -> None:
        """Test User __str__ method."""
        obj: Team = TeamFactory()
        expected_result = str(obj.name)
        assert expected_result == obj.__str__()
