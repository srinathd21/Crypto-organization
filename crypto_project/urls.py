from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import UserRegisterView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/register/', UserRegisterView.as_view(), name='user_register'),
    path('api/', include('core.urls.organization_urls')),
    path('api/', include('core.urls.crypto_price_urls')),
]
