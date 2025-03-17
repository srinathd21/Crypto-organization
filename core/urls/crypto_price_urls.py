from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.allViews.crypto_price_views import CryptoPriceViewSet

router = DefaultRouter()
router.register(r'crypto-prices', CryptoPriceViewSet, basename='crypto-price')

urlpatterns = [
    path('', include(router.urls)),
]
