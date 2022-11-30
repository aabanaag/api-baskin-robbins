from rest_framework import serializers

from baskin_robbins.branch.api.serializers import BranchSerializer
from baskin_robbins.inventory.models import Ingredient, Inventory
from baskin_robbins.product.models import Flavor, Product, Recipe, RecipeIngredient


class ProductIngredientRetrieveSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    quantity = serializers.DecimalField(
        source="get_quantity", max_digits=10, decimal_places=3, allow_null=True
    )

    class Meta:
        model = Ingredient
        fields = "__all__"


class ProductInventoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("quantity",)


class FlavorListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ("id", "name", "slug")


class ProductListRetrieveSerializer(serializers.ModelSerializer):
    flavor = FlavorListRetrieveSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    inventory = ProductInventoryRetrieveSerializer(read_only=True, many=True)

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


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class RecipeListRetrieveSerializer(serializers.ModelSerializer):
    product = ProductListRetrieveSerializer(read_only=True)
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class RecipeIngredientCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class RecipeIngredientListRetrieveSerializer(serializers.ModelSerializer):
    recipe = RecipeListRetrieveSerializer(read_only=True)
    ingredient = ProductIngredientRetrieveSerializer(read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
