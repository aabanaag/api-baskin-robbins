from django.db import models
from quantityfield.fields import QuantityField

from baskin_robbins.branch.models import Branch
from baskin_robbins.inventory.models import Ingredient


class Flavor(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class Product(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False, blank=False)
    sku = models.CharField(max_length=128)
    flavor = models.ForeignKey(
        Flavor, on_delete=models.CASCADE, null=False, blank=False
    )
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=False, blank=False
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=3, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku


class Recipe(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
    instructions = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, null=False, blank=False
    )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, null=False, blank=False
    )
    quantity = QuantityField(base_units="gram", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.recipe.name} - {self.ingredient.name}"
