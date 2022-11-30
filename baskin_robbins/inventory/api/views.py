from rest_framework.viewsets import ModelViewSet

from baskin_robbins.inventory.api.serializers import (
    IngredientCreateUpdateSerializer,
    IngredientListRetrieveSerializer,
    InventoryCreateUpdateSerializer,
    InventoryListRetrieveSerializer,
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


class InventoryViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()

    def get_queryset(self):
        return Ingredient.objects.prefetch_related("product").filter(
            product__branch=self.request.user.branch
        )  # noqa

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return InventoryListRetrieveSerializer
        return InventoryCreateUpdateSerializer
