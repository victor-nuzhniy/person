"""Fixtures for testing api app."""
from typing import Dict, Tuple

import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker

from api.models import User


@pytest.fixture
def get_authorized_admin_user_data(
    faker: Faker, django_user_model: User, client: Client
) -> Tuple[User, Dict]:
    """Create and get authorized user data for testing."""
    user = django_user_model.objects.create_superuser(
        email="test@gmail.com", password="password"
    )
    token_url: str = reverse("token")
    token_data: Dict = {"email": user.email, "password": "password"}
    response = client.post(token_url, data=token_data)
    access_token = response.json().get("access")
    headers: Dict = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    return user, headers


@pytest.fixture
def get_authorized_user_data(
    faker: Faker, django_user_model: User, client: Client
) -> Tuple[User, Dict]:
    """Create and get authorized user data for testing."""
    user = django_user_model.objects.create_user(
        email="test@gmail.com", password="password"
    )
    token_url: str = reverse("token")
    token_data: Dict = {"email": user.email, "password": "password"}
    response = client.post(token_url, data=token_data)
    access_token = response.json().get("access")
    headers: Dict = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    return user, headers
