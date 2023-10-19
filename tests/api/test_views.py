"""Module for testing api app views."""
import json
from typing import Dict, List, Tuple

import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker

from api.models import Team, User
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
class TestUserGetView:
    """Class for testing UserView get method."""

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

    def test_user_get_method_no_user(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView get method."""
        current_user, headers = get_authorized_admin_user_data
        url: str = reverse("user", kwargs={"pk": faker.random_int()})
        response = client.get(url, headers=headers)
        assert response.status_code == 404

    def test_user_get_method_unauthorized(
        self,
        faker: Faker,
        client: Client,
    ) -> None:
        """Test UserView get method."""
        url: str = reverse("user", kwargs={"pk": faker.random_int()})
        response = client.get(url)
        assert response.status_code == 401


@pytest.mark.django_db
class TestUserPutView:
    """Class for testing UserView put method."""

    pytestmark = pytest.mark.django_db

    def test_user_put_method(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView put method."""
        current_user, headers = get_authorized_admin_user_data
        user: User = UserFactory()
        team: Team = TeamFactory()
        data: Dict = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "team": team.pk,
        }
        url: str = reverse("user", kwargs={"pk": user.pk})
        response = client.put(url, headers=headers, data=json.dumps(data))
        result: Dict = response.json()
        assert response.status_code == 200
        for key, value in result.items():
            if key != "id":
                assert data[key] == value

    def test_user_put_method_not_full_data(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView put method."""
        current_user, headers = get_authorized_admin_user_data
        user: User = UserFactory()
        team: Team = TeamFactory()
        data: Dict = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "team": team.pk,
        }
        url: str = reverse("user", kwargs={"pk": user.pk})
        response = client.put(url, headers=headers, data=json.dumps(data))
        assert response.status_code == 400

    def test_user_put_method_not_admin_user(
        self,
        faker: Faker,
        client: Client,
        get_authorized_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView put method."""
        user: User = UserFactory()
        current_user, headers = get_authorized_user_data
        data: Dict = {}
        url: str = reverse("user", kwargs={"pk": user.pk})
        response = client.put(url, headers=headers, data=json.dumps(data))
        assert response.status_code == 403

    def test_user_put_method_unauthorized_user(
        self,
        faker: Faker,
        client: Client,
    ) -> None:
        """Test UserView put method."""
        user: User = UserFactory()
        data: Dict = {}
        url: str = reverse("user", kwargs={"pk": user.pk})
        response = client.put(url, data=json.dumps(data))
        assert response.status_code == 401


@pytest.mark.django_db
class TestUserPatchView:
    """Class for testing UserView patch method."""

    pytestmark = pytest.mark.django_db

    def test_user_patch_method(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView patch method."""
        current_user, headers = get_authorized_admin_user_data
        user: User = UserFactory()
        data: Dict = {"last_name": faker.last_name()}
        url: str = reverse("user", kwargs={"pk": user.pk})
        response = client.patch(url, headers=headers, data=json.dumps(data))
        result: Dict = response.json()
        assert response.status_code == 200
        assert result["last_name"] == data.get("last_name")


@pytest.mark.django_db
class TestUserDeleteView:
    """Class for testing UserView delete method."""

    pytestmark = pytest.mark.django_db

    def test_user_delete_method(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UserView delete method."""
        current_user, headers = get_authorized_admin_user_data
        user: User = UserFactory()
        url: str = reverse("user", kwargs={"pk": user.pk})
        response = client.delete(url, headers=headers)
        assert response.status_code == 204
        assert not User.objects.filter(id=user.pk).first()


@pytest.mark.django_db
class TestUsersView:
    """Class for testing UsersView get method."""

    pytestmark = pytest.mark.django_db

    def test_users_get_method(
        self,
        faker: Faker,
        client: Client,
        get_authorized_admin_user_data: Tuple[User, Dict],
    ) -> None:
        """Test UsersView get method."""
        current_user, headers = get_authorized_admin_user_data
        users: List[User] = UserFactory.create_batch(size=7)
        url: str = reverse("users")
        response = client.get(url, headers=headers)
        result: List = response.json()
        assert response.status_code == 200
        for i, user in enumerate(reversed(result)):
            if i == 7:
                break
            for key, value in user.items():
                if key == "team" and value:
                    assert getattr(users[-1 - i], key).id == value
                else:
                    assert getattr(users[-1 - i], key) == value
