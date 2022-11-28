from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from baskin_robbins.inventory.api.views import IngredientViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("ingredients", IngredientViewSet, basename="ingredient")

urlpatterns = router.urls
