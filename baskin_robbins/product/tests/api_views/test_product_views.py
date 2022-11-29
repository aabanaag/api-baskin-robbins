from django.urls import reverse
from factory.faker import faker
from rest_framework import status

from baskin_robbins.conftest import BaskinRobbinsTestCase
from baskin_robbins.product.tests.factories import FlavorFactory, ProductFactory

faker = faker.Faker()


class ProductViewTestCase(BaskinRobbinsTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.flavor = FlavorFactory.create()

        self.product = ProductFactory.create(branch=self.main_branch)

        ProductFactory.create_batch(9, branch=self.main_branch)

    def test_requires_authentication(self) -> None:
        url = reverse("api:product-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_product(self):
        url = reverse("api:product-list")
        auth = self._create_auth_header(self.staff.username)

        data = {
            "name": faker.word(),
            "description": faker.sentence(),
            "flavor": self.flavor.id,
            "sku": faker.ean(),
            "branch": self.main_branch.id,
            "price": faker.pydecimal(left_digits=2, right_digits=2),
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        product = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(product["name"], data["name"])
        self.assertEqual(product["sku"], data["sku"])

    def test_get_products(self):
        url = reverse("api:product-list")
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        products = response.json()["results"]
        product_count = response.json()["count"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product_count, len(products))

        # Make sure the each product info contains branch and flavor details
        for product in products:
            self.assertTrue(product["id"])
            self.assertTrue(product["branch"])
            self.assertTrue(product["flavor"])

    def test_get_product(self):
        url = reverse("api:product-detail", kwargs={"pk": self.product.id})
        auth = self._create_auth_header(self.staff.username)

        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        product = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(product["id"])
        self.assertTrue(product["branch"]["id"])
        self.assertTrue(product["flavor"]["id"])

    def test_update_product(self):
        url = reverse("api:product-detail", kwargs={"pk": self.product.id})
        auth = self._create_auth_header(self.staff.username)

        new_flavor = FlavorFactory.create()
        data = {
            "flavor": new_flavor.id,
        }

        response = self.client.patch(url, data, HTTP_AUTHORIZATION=auth)
        product = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Make sure the product details are the same
        self.assertTrue(product["id"])
        self.assertTrue(product["branch"])

        # Make sure the new flavor is set
        self.assertEqual(product["flavor"], new_flavor.id)

    def test_delete_product(self):
        url = reverse("api:product-detail", kwargs={"pk": self.product.id})
        auth = self._create_auth_header(self.staff.username)

        response = self.client.delete(url, HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
