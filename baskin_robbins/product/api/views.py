from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from baskin_robbins.product.api.serializers import (
    ProductCreateUpdateSerializer,
    ProductListRetrieveSerializer,
    RecipeCreateUpdateSerializer,
    RecipeIngredientCreateUpdateSerializer,
    RecipeIngredientListRetrieveSerializer,
    RecipeListRetrieveSerializer,
)
from baskin_robbins.product.models import Product, Recipe, RecipeIngredient
from baskin_robbins.product.services import process_purchase
from baskin_robbins.utils.exceptions import ProductNoInventory


class ProductViewSet(ModelViewSet):
    def get_queryset(self):
        return Product.objects.filter(branch=self.request.user.branch)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductListRetrieveSerializer
        return ProductCreateUpdateSerializer

    @action(detail=True, methods=["post"])
    @permission_classes([IsAuthenticated])
    def buy(self):
        try:
            product = self.get_object()
            quantity = self.request.data.get("quantity", 1)
            is_success = process_purchase(product=product, quantity=quantity)
            return Response(
                "Enjoy!" if is_success else "Unable to process order",
                status=status.HTTP_200_OK,
            )
        except ProductNoInventory:
            return Response(
                "Insufficient inventory", status=status.HTTP_400_BAD_REQUEST
            )


class RecipeViewSet(ModelViewSet):
    def get_queryset(self):
        return Recipe.objects.prefetch_related("product").filter(
            product__branch=self.request.user.branch
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return RecipeListRetrieveSerializer
        return RecipeCreateUpdateSerializer


class RecipeIngredientViewSet(ModelViewSet):
    def get_queryset(self):
        return RecipeIngredient.objects.prefetch_related("recipe").filter(
            recipe__product__branch=self.request.user.branch
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return RecipeIngredientListRetrieveSerializer
        return RecipeIngredientCreateUpdateSerializer
