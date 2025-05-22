

# Create your models here.
from django.db import models
from django.conf import settings
from django.apps import apps
from store.models import Store





class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} (x{self.quantity})"
