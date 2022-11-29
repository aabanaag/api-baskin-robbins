from rest_framework import serializers

from baskin_robbins.branch.api.serializers import BranchSerializer
from baskin_robbins.product.models import Flavor, Product, Recipe, RecipeIngredient


class FlavorListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ("id", "name", "slug")


class ProductListRetrieveSerializer(serializers.ModelSerializer):
    flavor = FlavorListRetrieveSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "flavor", "branch", "name", "description", "sku", "price")
        read_only_fields = ("id", "created_at", "updated_at")


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
