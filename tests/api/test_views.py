"""Module for testing api app views."""
from typing import Dict, List, Tuple

import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker

from api.models import User
from tests.api.factories import TeamFactory, UserFactory


@pytest.mark.django_db
class TestRegisterView:
    """Class for testing RegisterView."""

    pytestmark = pytest.mark.django_db

    def test_register_view(self, faker: Faker, client: Client) -> None:
        """Test RegisterView."""
        data: Dict = {
            "email": faker.email(),
            "password": faker.pystr(min_chars=1, max_chars=40),
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "team": TeamFactory().id,
        }
        url: str = reverse("sign_up")
        response = client.post(url, data=data)
        result: Dict = response.json()
        assert response.status_code == 201
        for key, value in data.items():
            if key != "password":
                assert result[key] == value

    def test_register_view_without_names(self, faker: Faker, client: Client) -> None:
        """Test RegisterView."""
        data: Dict = {
            "email": faker.email(),
            "password": faker.pystr(min_chars=1, max_chars=40),
        }
        url: str = reverse("sign_up")
        response = client.post(url, data=data)
        result: Dict = response.json()
        assert response.status_code == 201
        assert result.get("email") == data.get("email")

    def test_register_view_invalid_email(self, faker: Faker, client: Client) -> None:
        """Test RegisterView."""
        data: Dict = {
            "email": faker.pystr(min_chars=1, max_chars=10),
            "password": faker.pystr(min_chars=1, max_chars=40),
        }
        url: str = reverse("sign_up")
        response = client.post(url, data=data)
        assert response.status_code == 400

    def test_register_view_unique_email(self, faker: Faker, client: Client) -> None:
        """Test RegisterView."""
        user = UserFactory()
        data: Dict = {
            "email": user.email,
            "password": faker.pystr(min_chars=1, max_chars=40),
        }
        url: str = reverse("sign_up")
        response = client.post(url, data=data)
        assert response.status_code == 400

    def test_register_view_empty_password(self, faker: Faker, client: Client) -> None:
        """Test RegisterView."""
        data: Dict = {
            "email": faker.email(),
        }
        url: str = reverse("sign_up")
        response = client.post(url, data=data)
        assert response.status_code == 400


@pytest.mark.django_db
class TestUserView:
    """Class for testing UserView methods."""

    pytestmark = pytest.mark.django_db

    def test_user_get_method(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView get method."""
        current_user, headers = get_authorized_admin_user_data
        users: List[User] = UserFactory.create_batch(size=5)
        user = faker.random_element(elements=users)
        url: str = reverse("user", kwargs={"pk": user.id})
        response = client.get(url, headers=headers)
        result: Dict = response.json()
        assert response.status_code == 200
        for key, value in result.items():
            if key == "team":
                assert getattr(user, key).id == value
            else:
                assert getattr(user, key) == value
