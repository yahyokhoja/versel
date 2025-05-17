from django.contrib import admin
from .models import Store, Category, SubCategory, Product

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'subcategory')
    list_filter = ('subcategory',)
    search_fields = ('name', 'description')

admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
