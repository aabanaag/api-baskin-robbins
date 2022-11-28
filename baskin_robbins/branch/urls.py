from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from baskin_robbins.branch.api.views import BranchViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("branches", BranchViewSet, basename="branch")

urlpatterns = router.urls
