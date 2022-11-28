from factory import (  # noqa
    Faker,
)
from rest_framework import status
from django.urls import reverse

from baskin_robbins.conftest import BaskinRobbinsTestCase
from baskin_robbins.branch.tests.factories import BranchFactory


class BranchViewTestCase(BaskinRobbinsTestCase):
    def setupTestData(self):
        self.branch = BranchFactory.create()

    def test_get_branches(self):
        url = reverse("api:branch-list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
