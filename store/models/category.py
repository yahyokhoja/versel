from django.db import models
from .store import Store

class Category(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='categories')  # Оставляем как есть

    def __str__(self):
        return f"{self.name} ({self.store.name})"

    class Meta:
        indexes = [
            models.Index(fields=['store']),
        ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
