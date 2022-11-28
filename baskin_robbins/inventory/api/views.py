from rest_framework.viewsets import ModelViewSet

from baskin_robbins.inventory.api.serializers import (
    IngredientCreateUpdateSerializer,
    IngredientListRetrieveSerializer,
)
from baskin_robbins.inventory.models import Ingredient


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()

    def get_queryset(self):
        return Ingredient.objects.filter(branch=self.request.user.branch)  # noqa

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return IngredientListRetrieveSerializer
        return IngredientCreateUpdateSerializer
