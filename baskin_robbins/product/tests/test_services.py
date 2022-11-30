"""
Product - service test
"""

from factory.faker import faker

from baskin_robbins.conftest import BaskinRobbinsTestCase
from baskin_robbins.inventory.models import Inventory
from baskin_robbins.inventory.tests.factories import InventoryFactory
from baskin_robbins.product.services import process_purchase
from baskin_robbins.product.tests.factories import (
    ProductFactory,
    TransactionWithProductFactory,
)
from baskin_robbins.utils.exceptions import ProductNoInventory

faker = faker.Faker()


class ProductServiceTestCase(BaskinRobbinsTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.product = ProductFactory.create(branch=self.main_branch)

        InventoryFactory.create(product=self.product, quantity=10)

        self.transaction = TransactionWithProductFactory.create(product=self.product)

        TransactionWithProductFactory.create_batch(9)

    def test_process_purchase(self):
        process_purchase(self.product, 1)

        inventory = Inventory.objects.filter(product=self.product)

        self.assertTrue(inventory.exists())
        self.assertEqual(inventory.first().quantity, 9)

        self.assertEqual(self.product.transactions.count(), 2)

    def test_purchase_should_fail(self):
        with self.assertRaises(ProductNoInventory):
            is_success = process_purchase(self.ice_cream, 1)

            self.assertFalse(is_success)
