from django.db import models
from users.models import CustomUser
from .store import Store


class StoreOwnerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='store_owner_profile')  # Связь с пользователем
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='owner_profile')  # Связь с магазином
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Телефон владельца (опционально)
    address = models.TextField(blank=True, null=True)  # Адрес владельца (опционально)
    additional_info = models.TextField(blank=True, null=True)  # Дополнительная информация (опционально)

    def __str__(self):
        return f"Профиль владельца: {self.user.username}"
