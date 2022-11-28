import pytest
from allauth.account import app_settings as account_settings
from django.test.utils import override_settings
from django.urls import reverse
from rest_framework.test import APITestCase

from baskin_robbins.branch.tests.factories import BranchFactory
from baskin_robbins.users.models import User
from baskin_robbins.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


class BaskinRobbinsTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.main_branch = BranchFactory.create()
        self.staff = UserFactory.create(password="password", branch=self.main_branch)

    @override_settings(
        ACCOUNT_EMAIL_VERIFICATION=account_settings.EmailVerificationMethod.NONE  # noqa
    )
    def _create_auth_header(self, username: str, password: str = "password") -> str:
        url = reverse("api:rest_login")
        data = {"username": username, "password": password}

        response = self.client.post(url, data, format="json")
        token = response.json()["access_token"]

        return f"Bearer {token}"
