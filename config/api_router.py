from allauth.account.views import ConfirmEmailView
from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from baskin_robbins.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "auth/registration/confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("", include("baskin_robbins.branch.urls")),
    path("", include("baskin_robbins.inventory.urls")),
] + router.urls
