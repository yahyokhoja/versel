from django.db import models
from store.models import Product
from users.models import CustomUser  # Импортируем кастомную модель пользователя

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидает'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
