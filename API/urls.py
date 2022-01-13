from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ArtistViewSet, CountryViewSet, UserViewSet


router = DefaultRouter()

router.register(r"countries", CountryViewSet, basename="countries")
router.register(r"users", UserViewSet, basename="users")
router.register(r"artists", ArtistViewSet, basename="artists")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
