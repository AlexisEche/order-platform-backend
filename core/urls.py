
from django.contrib import admin
from django.urls import path

from django.urls.conf import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
API_BASE_URL = "api/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path(f"{API_BASE_URL}", include("apps.account.urls"), name="account"),
    path(f"{API_BASE_URL}", include("apps.recipes.urls"), name="recipes"),
]
