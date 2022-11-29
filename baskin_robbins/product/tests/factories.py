from django.utils.text import slugify
from factory import Faker, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory

from baskin_robbins.branch.tests.factories import BranchFactory
from baskin_robbins.product.models import Flavor, Product


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
