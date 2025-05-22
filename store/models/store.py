
# store/models.py

from django.db import models
from users.models import CustomUser  # импортируем кастомную модель пользователя

class Store(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='store')  # связь с владельцем
    name = models.CharField(max_length=255)  # Название магазина
    description = models.TextField(blank=True)  # Описание магазина
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания магазина
    logo = models.ImageField(upload_to='store_logos/', null=True, blank=True)  # Логотип магазина (опционально)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
  # Дополнительная информация (опционально)

   
    def __str__(self):
        return self.name  # ← оставить только это
