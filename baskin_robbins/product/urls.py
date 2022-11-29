from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from baskin_robbins.product.api.views import ProductViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("products", ProductViewSet, basename="product")

urlpatterns = router.urls
