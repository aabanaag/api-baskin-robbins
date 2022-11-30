from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from baskin_robbins.branch.tests.factories import BranchFactory
from baskin_robbins.inventory.models import Ingredient, Inventory


class IngredientFactory(DjangoModelFactory):
    name = Faker("word")
    description = Faker("sentence")
    quantity = Faker("pydecimal", left_digits=3, right_digits=3, positive=True)
    branch = SubFactory(BranchFactory)

    class Meta:
        model = Ingredient


class InventoryFactory(DjangoModelFactory):
    product = SubFactory("baskin_robbins.product.tests.factories.ProductFactory")
    quantity = Faker("pyint", min_value=0, max_value=100)

    class Meta:
        model = Inventory
