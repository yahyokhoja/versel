

from django.shortcuts import render
from django.shortcuts import render
from .models import Category, Product, SubCategory

def index(request):
    return render(request, 'asosi/index.html')

def products_by_subcategory(request, subcategory_id):
    products = Product.objects.filter(subcategory_id=subcategory_id)
    return render(request, 'asosi/products_list.html', {'products': products})


