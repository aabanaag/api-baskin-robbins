from decimal import Decimal

from django.db import models
from quantityfield.fields import QuantityField

from baskin_robbins.branch.models import Branch
from baskin_robbins.product.models import Product


class Ingredient(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False, blank=False)
    quantity = QuantityField(
        base_units="gram",
        null=False,
        blank=False,
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_quantity(self) -> Decimal:
        return self.quantity.magnitude


class Inventory(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="inventory",
    )
    quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
