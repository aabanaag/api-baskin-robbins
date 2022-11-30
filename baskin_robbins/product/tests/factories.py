from django.utils.text import slugify
from factory import Faker, LazyAttribute, RelatedFactory, SubFactory
from factory.django import DjangoModelFactory

from baskin_robbins.branch.tests.factories import BranchFactory
from baskin_robbins.inventory.tests.factories import IngredientFactory
from baskin_robbins.product.models import (
    Flavor,
    Product,
    Recipe,
    RecipeIngredient,
    Transaction,
)


class FlavorFactory(DjangoModelFactory):
    name = Faker("word")
    slug = LazyAttribute(lambda o: slugify(o.name))

    class Meta:
        model = Flavor
        django_get_or_create = ("name",)


class ProductFactory(DjangoModelFactory):
    name = Faker("word")
    description = Faker("sentence")
    sku = Faker("ean")
    flavor = SubFactory(FlavorFactory)
    branch = SubFactory(BranchFactory)
    price = Faker("pydecimal", left_digits=2, right_digits=2, positive=True)

    class Meta:
        model = Product


class RecipeFactory(DjangoModelFactory):
    product = SubFactory(ProductFactory)

    class Meta:
        model = Recipe


class RecipeIngredientFactory(DjangoModelFactory):
    recipe = SubFactory(RecipeFactory)
    ingredient = SubFactory(IngredientFactory)
    quantity = Faker("pydecimal", left_digits=2, right_digits=2, positive=True)

    class Meta:
        model = RecipeIngredient


class RecipeWithIngredientFactory(RecipeFactory):
    recipe_ingredient = RelatedFactory(RecipeIngredientFactory, "recipe")


class TransactionWithProductFactory(DjangoModelFactory):
    product = SubFactory(ProductFactory)
    quantity = Faker("pyint", min_value=1, max_value=10)

    class Meta:
        model = Transaction
