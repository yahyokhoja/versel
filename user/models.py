

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_store_admin = models.BooleanField(default=False)
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL, related_name='users')
