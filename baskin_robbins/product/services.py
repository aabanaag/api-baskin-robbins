"""
Product - Service
"""

from baskin_robbins.product.models import Product, Transaction
from baskin_robbins.utils.exceptions import ProductNoInventory


def process_purchase(product: Product, quantity: int):
    if product.has_inventory():
        """
        @TODO: Add logic to handle inventory, make sure to perform FIFO
        """
        inventory = product.inventory.order_by("-created_at").first()
        inventory.quantity -= quantity
        inventory.save()

        Transaction.objects.create(product=product, quantity=quantity)
    else:
        raise ProductNoInventory()
