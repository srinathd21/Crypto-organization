from rest_framework import viewsets, permissions
from core.models import CryptoPrice, Organization
from core.serializers.crypto_price_serializer import CryptoPriceSerializer

class CryptoPriceViewSet(viewsets.ModelViewSet):
    serializer_class = CryptoPriceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_orgs = Organization.objects.filter(owner=self.request.user)
        return CryptoPrice.objects.filter(org__in=user_orgs)
