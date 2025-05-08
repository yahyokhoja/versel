from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory, Store

# Главная страница
def index(request):
    stores = Store.objects.prefetch_related('categories__subcategories').all()
    return render(request, 'asosi/index.html', {'stores': stores})

# Страница с продуктами по подкатегории
def products_by_subcategory(request, subcategory_id):
    # Получаем подкатегорию по id
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)

    # Получаем все продукты этой подкатегории
    products = Product.objects.filter(subcategory=subcategory)

    # Отображаем продукты на странице
    return render(request, 'asosi/products_list.html', {
        'subcategory': subcategory,
        'products': products
    })
