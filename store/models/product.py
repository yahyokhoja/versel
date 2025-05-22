from django.db import models
from .category import SubCategory
from store.models import Store

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE, default=1)  # Значение по умолчанию, которое будет установлено для старых продуктов
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Поле для изображения
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
