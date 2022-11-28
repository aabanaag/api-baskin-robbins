from decimal import Decimal

from django.urls import reverse
from factory.faker import faker
from rest_framework import status

from baskin_robbins.conftest import BaskinRobbinsTestCase
from baskin_robbins.inventory.tests.factories import IngredientFactory

faker = faker.Faker()


class IngredientViewTestCase(BaskinRobbinsTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.milk = IngredientFactory.create(name="Milk", branch=self.main_branch)
        self.sugar = IngredientFactory.create(name="Sugar", branch=self.main_branch)

        self.ingredients = IngredientFactory.create_batch(7, branch=self.main_branch)

    def test_requires_authentication(self) -> None:
        url = reverse("api:ingredient-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_ingredient(self):
        url = reverse("api:ingredient-list")
        auth = self._create_auth_header(self.staff.username)

        data = {
            "name": "cream",
            "description": faker.sentence(),
            "quantity": faker.pydecimal(3, 3, True),
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        ingredient = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ingredient["name"], data["name"])
        self.assertEqual(ingredient["description"], data["description"])
        self.assertEqual(str(ingredient["quantity"]), str(data["quantity"]))

    def test_get_ingredients(self):
        url = reverse("api:ingredient-list")
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)

        ingredient_count = response.json()["count"]
        ingredients = response.json()["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ingredient_count, len(ingredients))

    def test_get_ingredient(self):
        url = reverse("api:ingredient-detail", kwargs={"pk": self.milk.id})
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        ingredient = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ingredient["name"], self.milk.name)
        self.assertEqual(ingredient["description"], self.milk.description)
        self.assertEqual(Decimal(ingredient["quantity"]), self.milk.quantity)
        self.assertTrue(ingredient["branch"]["id"])

    def test_update_ingredient(self):
        url = reverse("api:ingredient-detail", kwargs={"pk": self.milk.id})
        auth = self._create_auth_header(self.staff.username)

        data = {
            "quantity": faker.pydecimal(3, 3, True),
        }

        response = self.client.patch(url, data, HTTP_AUTHORIZATION=auth)
        ingredient = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ingredient["name"], self.milk.name)
        self.assertEqual(ingredient["description"], self.milk.description)
        self.assertEqual(str(round(ingredient["quantity"], 3)), str(data["quantity"]))
