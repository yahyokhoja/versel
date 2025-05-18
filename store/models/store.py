from django.db import models
from user.models import CustomUser  # импортируем кастомную модель пользователя

class Store(models.Model):
    # Изменили related_name на 'store_owner', чтобы избежать конфликта
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='store_owner')  
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='store_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
