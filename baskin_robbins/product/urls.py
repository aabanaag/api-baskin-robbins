from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from baskin_robbins.product.api.views import (
    ProductViewSet,
    RecipeIngredientViewSet,
    RecipeViewSet,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("products", ProductViewSet, basename="product")
router.register("recipes", RecipeViewSet, basename="recipe")
router.register(
    "recipe-ingredients", RecipeIngredientViewSet, basename="recipe-ingredient"
)

urlpatterns = router.urls
