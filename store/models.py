# store/models.py

from django.db import models
from user.models import CustomUser

class Store(models.Model):
    owner = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='store'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StoreOwnerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='store_owner_profile'
    )
    store = models.OneToOneField(
        Store,
        on_delete=models.CASCADE,
        related_name='owner_profile'
    )

    # Добавь поля при необходимости (телефон, адрес и т.д.)
    def __str__(self):
        return f"Профиль владельца: {self.user.username}"
