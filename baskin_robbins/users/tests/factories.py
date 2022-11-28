from django.contrib.auth import get_user_model
from factory import Faker, PostGenerationMethodCall, SubFactory
from factory.django import DjangoModelFactory

from baskin_robbins.branch.tests.factories import BranchFactory


class UserFactory(DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    password = PostGenerationMethodCall("set_password", "password")
    branch = SubFactory(BranchFactory)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
