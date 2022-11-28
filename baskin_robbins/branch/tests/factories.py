from django.utils.text import slugify
from factory import (
    Faker,
    LazyAttribute
)
from factory.django import DjangoModelFactory
from baskin_robbins.branch.models import Branch


class BranchFactory(DjangoModelFactory):
    name = Faker("company")
    slug = LazyAttribute(lambda o: slugify(o.name))

    class Meta:
        model = Branch
