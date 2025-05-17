from django.db import models
from user.models import CustomUser  # Импорт кастомной модели пользователя

# Профиль владельца магазина (если нужно хранить что-то еще о владельце в будущем)
class StoreOwnerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='store_profile')
    store = models.OneToOneField('Store', on_delete=models.CASCADE, related_name='owner_profile')

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Модель магазина
class Store(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='store')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='store_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

# Категория товаров
class Category(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f"{self.name} ({self.store.name})"

    class Meta:
        indexes = [
            models.Index(fields=['store']),
        ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Подкатегория товаров
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

# Продукт
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
