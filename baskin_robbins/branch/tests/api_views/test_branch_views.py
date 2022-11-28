from django.urls import reverse
from django.utils.text import slugify
from factory.faker import faker
from rest_framework import status

from baskin_robbins.branch.tests.factories import BranchFactory
from baskin_robbins.conftest import BaskinRobbinsTestCase

faker = faker.Faker()


class BranchViewTestCase(BaskinRobbinsTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.branch = BranchFactory.create()

    def test_requires_authentication(self) -> None:
        url = reverse("api:branch-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_branch(self):
        url = reverse("api:branch-list")
        auth = self._create_auth_header(self.staff.username)

        data = {"name": faker.company()}
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        branch = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(branch["name"], data["name"])
        self.assertEqual(branch["slug"], slugify(data["name"]))

    def test_get_branches(self):
        url = reverse("api:branch-list")
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        branches = response.json()["results"]
        branches_count = response.json()["count"]

        self.assertEqual(branches_count, len(branches))

    def test_get_branch(self):
        url = reverse("api:branch-detail", kwargs={"pk": self.branch.id})
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        branch = response.json()
        self.assertEqual(branch["id"], self.branch.id)
        self.assertEqual(self.branch.slug, slugify(branch["name"]))

    def test_update_branch(self):
        url = reverse("api:branch-detail", kwargs={"pk": self.branch.id})
        auth = self._create_auth_header(self.staff.username)

        data = {"name": faker.word()}

        response = self.client.patch(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        branch = response.json()
        self.assertEqual(branch["id"], self.branch.id)
        self.assertNotEqual(branch["name"], self.branch.name)
        self.assertEqual(branch["slug"], slugify(data["name"]))

    def test_delete_branch(self):
        url = reverse("api:branch-detail", kwargs={"pk": self.branch.id})
        auth = self._create_auth_header(self.staff.username)

        response = self.client.delete(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
