from django.urls import reverse
from factory.faker import faker
from rest_framework import status

from baskin_robbins.conftest import BaskinRobbinsTestCase
from baskin_robbins.product.tests.factories import RecipeWithIngredientFactory

faker = faker.Faker()


class RecipeViewTestCase(BaskinRobbinsTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.recipe = RecipeWithIngredientFactory.create(product=self.ice_cream)

        RecipeWithIngredientFactory.create_batch(9, product=self.ice_cream)

    def test_requires_authentication(self) -> None:
        url = reverse("api:product-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_recipes(self):
        url = reverse("api:recipe-list")
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        recipes = response.json()["results"]
        recipe_count = response.json()["count"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(recipe_count, len(recipes))

    def test_create_recipe(self):
        url = reverse("api:recipe-list")
        auth = self._create_auth_header(self.staff.username)

        data = {
            "name": faker.word(),
            "description": faker.sentence(),
            "product": self.ice_cream.id,
            "instructions": faker.sentence(),
        }

        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_recipe(self):
        url = reverse("api:recipe-list")
        auth = self._create_auth_header(self.staff.username)

        data = {
            "name": faker.word(),
            "description": faker.sentence(),
            "product": self.ice_cream.id,
            "instructions": faker.sentence(),
        }

        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
