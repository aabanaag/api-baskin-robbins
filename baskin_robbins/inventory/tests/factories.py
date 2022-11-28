from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from baskin_robbins.branch.tests.factories import BranchFactory
from baskin_robbins.inventory.models import Ingredient


class IngredientFactory(DjangoModelFactory):
    name = Faker("word")
    description = Faker("sentence")
    quantity = Faker("pydecimal", left_digits=3, right_digits=3, positive=True)
    branch = SubFactory(BranchFactory)

    class Meta:
        model = Ingredient
