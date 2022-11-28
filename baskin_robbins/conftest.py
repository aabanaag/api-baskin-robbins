import pytest

from rest_framework.test import APITestCase
from django.urls import reverse

from baskin_robbins.users.models import User
from baskin_robbins.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


class BaskinRobbinsTestCase(APITestCase):
    def setupTestData(self):
        self.user = UserFactory()

    def _create_auth_header(self, username: str, password: str = "password") -> str:
        url = reverse("api:rest_login")
        data = {"username": username, "password": password}

        response = self.client.post(url, data, format="json")
        token = response.json()["access_token"]

        return f"Bearer {token}"
