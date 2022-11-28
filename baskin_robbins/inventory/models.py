from decimal import Decimal

from django.db import models
from quantityfield.fields import QuantityField

from baskin_robbins.branch.models import Branch


class Ingredient(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False, blank=False)
    quantity = QuantityField(
        base_units="gram",
        null=False,
        blank=False,
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_quantity(self) -> Decimal:
        return self.quantity.magnitude

    class Meta:
        ordering = ["name"]
