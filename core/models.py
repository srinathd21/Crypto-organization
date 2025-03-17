from django.db import models
import uuid
from django.contrib.auth.models import User


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CryptoPrice(models.Model):
    id = models.AutoField(primary_key=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)
