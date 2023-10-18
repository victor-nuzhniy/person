"""Module for api app urls."""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import RegisterView

urlpatterns = [
    path("auth/token/", TokenObtainPairView.as_view(), name="token"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/signup/", RegisterView.as_view(), name="sign_up"),
]
