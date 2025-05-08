
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory, Store

# Главная страница
def index(request):
    stores = Store.objects.prefetch_related('categories__subcategories').all()
    return render(request, 'asosi/index.html', {'stores': stores})

# Страница с продуктами по подкатегории
def products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'asosi/products_list.html', {'subcategory': subcategory, 'products': products})

# Страница детального магазина
def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'asosi/store_detail.html', {'store': store})