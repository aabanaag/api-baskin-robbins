"""
Product - service test
"""

from factory.faker import faker

from baskin_robbins.conftest import BaskinRobbinsTestCase
from baskin_robbins.inventory.tests.factories import InventoryFactory
from baskin_robbins.product.services import process_purchase
from baskin_robbins.product.tests.factories import (
    ProductFactory,
    TransactionWithProductFactory,
)

faker = faker.Faker()


class ProductServiceTestCase(BaskinRobbinsTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.product = ProductFactory.create(branch=self.main_branch)

        InventoryFactory.create_batch(10, product=self.product)

        self.transaction = TransactionWithProductFactory.create(product=self.product)

        TransactionWithProductFactory.create_batch(9)

    def test_process_purchase(self):
        process_purchase(self.product, 1)

        print(self.product.inventory)
        self.assertEqual(self.product.transactions.count(), 2)
