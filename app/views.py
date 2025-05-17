
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory, Store
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import StoreCreateForm
from .models import Store

@login_required
def create_store_view(request):
    if request.user.role != 'store_owner':
        return redirect('home')  # Запрет для обычных пользователей

    # Проверка: не создал ли он уже магазин?
    if hasattr(request.user, 'store'):
        return redirect('store_detail', store_id=request.user.store.id)

    if request.method == 'POST':
        form = StoreCreateForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = StoreCreateForm()

    return render(request, 'app/create_store.html', {'form': form})




# Главная страница
def index(request):
    stores = Store.objects.prefetch_related('categories__subcategories').all()
    return render(request, 'app/index.html', {'stores': stores})

# Страница с продуктами по подкатегории
def products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'app/products_list.html', {'subcategory': subcategory, 'products': products})

# Страница детального магазина
def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'app/store_detail.html', {'store': store})