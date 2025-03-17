from rest_framework import serializers
from core.models import CryptoPrice

class CryptoPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPrice
        fields = '__all__'
