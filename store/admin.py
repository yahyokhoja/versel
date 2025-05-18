

# Register your models here.
from django.contrib import admin
from .models import Store, StoreOwnerProfile, Category, SubCategory, Product

admin.site.register(Store)
admin.site.register(StoreOwnerProfile)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
