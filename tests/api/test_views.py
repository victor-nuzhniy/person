"""Module for testing api app views."""
from typing import Dict

import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker

from tests.api.factories import TeamFactory


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
