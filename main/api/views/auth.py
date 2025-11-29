from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from main.api.constants import TAGS


class AuthTokenObtainPairView(TokenObtainPairView):
    @extend_schema(tags=[TAGS.AUTHENTICATION])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AuthTokenRefreshView(TokenRefreshView):
    @extend_schema(tags=[TAGS.AUTHENTICATION])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AuthTokenVerifyView(TokenVerifyView):
    @extend_schema(tags=[TAGS.AUTHENTICATION])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
