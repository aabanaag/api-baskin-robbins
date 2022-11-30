from rest_framework import serializers

from baskin_robbins.branch.api.serializers import BranchSerializer
from baskin_robbins.inventory.models import Ingredient, Inventory
from baskin_robbins.product.models import Product


class IngredientListRetrieveSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    quantity = serializers.DecimalField(
        source="get_quantity", max_digits=10, decimal_places=3, allow_null=True
    )

    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "description", "branch", "quantity")
        read_only_fields = ("created", "modified")


class InventoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("id", "product", "quantity")
        read_only_fields = ("created", "modified")


class ProductListRetrieveSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class InventoryListRetrieveSerializer(serializers.ModelSerializer):
    product = ProductListRetrieveSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"
