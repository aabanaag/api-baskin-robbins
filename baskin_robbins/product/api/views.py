from rest_framework.viewsets import ModelViewSet

from baskin_robbins.product.api.serializers import (
    ProductCreateUpdateSerializer,
    ProductListRetrieveSerializer,
    RecipeIngredientSerializer,
    RecipeSerializer,
)
from baskin_robbins.product.models import Product, Recipe, RecipeIngredient


class ProductViewSet(ModelViewSet):
    def get_queryset(self):
        return Product.objects.filter(branch=self.request.user.branch)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductListRetrieveSerializer
        return ProductCreateUpdateSerializer


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.prefetch_related("product").filter(
            product__branch=self.request.user.branch
        )


class RecipeIngredientViewSet(ModelViewSet):
    serializer_class = RecipeIngredientSerializer

    def get_queryset(self):
        return RecipeIngredient.objects.prefetch_related("recipe").filter(
            recipe__product__branch=self.request.user.branch
        )
