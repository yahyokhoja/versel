from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StoreForm, ProductForm
from .models import Store, Product
from django.shortcuts import render, get_object_or_404
from .models import Product, SubCategory  # убедитесь, что SubCategory у вас есть

def products_by_subcategory(request, subcategory_id):
    # Предположим, у вас есть модель SubCategory и связь с Product
    products = Product.objects.filter(subcategory_id=subcategory_id)
    return render(request, 'store/products_by_subcategory.html', {'products': products})





def store_detail_view(request, store_id):
    try:
        # Получаем магазин по store_id
        store = get_object_or_404(Store, id=store_id)
    except Store.DoesNotExist:
        store = None

    # Если у пользователя уже есть магазин, перенаправляем его на дашборд
    if store and store.owner == request.user:
        return redirect('store_dashboard')  # Редирект на дашборд

    # Если магазин найден и не принадлежит текущему пользователю
    return render(request, 'store/store_detail.html', {'store': store})

@login_required
def store_dashboard_view(request):
    try:
        store = Store.objects.get(owner=request.user)
    except Store.DoesNotExist:
        return redirect('create_store')  # если у пользователя нет магазина

    # получаем все товары магазина (если есть такая модель)
    products = Product.objects.filter(store=store)

    return render(request, 'store/dashboard.html', {
        'store': store,
        'products': products,
    })
@login_required
def create_store_view(request):
    try:
        # Если у пользователя уже есть магазин, отправляем его на дашборд
        existing_store = Store.objects.get(owner=request.user)
        return redirect('store_dashboard')
    except Store.DoesNotExist:
        pass  # Магазина нет — показываем форму для создания

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = StoreForm()

    return render(request, 'store/create_store.html', {'form': form})


@login_required
def add_product_view(request):
    # Получаем магазин пользователя
    store = get_object_or_404(Store, owner=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store  # Привязываем продукт к магазину
            product.save()
            return redirect('store_dashboard')  # Перенаправляем в панель магазина
    else:
        form = ProductForm()
    
    return render(request, 'store/add_product.html', {'form': form})

@login_required
def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')  # Перенаправляем в панель магазина
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'store/edit_product.html', {'form': form, 'product': product})

@login_required
def edit_store_view(request, store_id):
    store = get_object_or_404(Store, id=store_id, owner=request.user)

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = StoreForm(instance=store)

    return render(request, 'store/edit_store.html', {'form': form, 'store': store})