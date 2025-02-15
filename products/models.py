from django.db import models
from django.conf import settings

class Product(models.Model):
    SIZE_CHOICES = [("small", "Small"), ("large", "Large")]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.TextField()
    barcode = models.CharField(max_length=30, unique=True)
    expiration_date = models.DateField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
