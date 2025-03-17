import requests
from celery import shared_task
from .models import CryptoPrice, Organization
from decimal import Decimal
from django.utils.timezone import now

@shared_task
def fetch_crypto_prices():
    print("🔄 Fetching crypto prices...") 
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        btc_price = Decimal(data["bitcoin"]["usd"])
        eth_price = Decimal(data["ethereum"]["usd"])

        print(f"✅ BTC: {btc_price}, ETH: {eth_price}") 

        organizations = Organization.objects.all()
        if not organizations.exists():
            print("⚠️ No organizations found. Prices cannot be saved.")
            return
        
        for org in organizations:
            CryptoPrice.objects.create(org=org, symbol="BTC", price=btc_price, timestamp=now())
            CryptoPrice.objects.create(org=org, symbol="ETH", price=eth_price, timestamp=now())

        print("✅ Crypto prices saved successfully!")

    except Exception as e:
        print(f"❌ Error fetching crypto prices: {e}")
