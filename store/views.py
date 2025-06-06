from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StoreForm, ProductForm, SubCategoryForm
from .models import Store, Product


# Отображение товаров по подкатегории
def products_by_subcategory(request, subcategory_id):
    # Предположим, что SubCategory у вас существует и связь с Product работает корректно
    products = Product.objects.filter(subcategory_id=subcategory_id)
    return render(request, 'store/products_by_subcategory.html', {'products': products})


# Детали магазина (если магазин существует и не принадлежит текущему пользователю, редиректим)
def store_detail_view(request, store_id):
    # Получаем магазин по ID или возвращаем 404, если он не найден
    store = get_object_or_404(Store, id=store_id)
    
    # Если магазин принадлежит текущему пользователю, перенаправляем на дашборд
    if store.owner == request.user:
        return redirect('store_dashboard')  # Перенаправляем на панель управления магазина

    # Если магазин не принадлежит текущему пользователю, отображаем детали магазина
    return render(request, 'store/store_detail.html', {'store': store})

# Панель управления магазином
@login_required
def store_dashboard_view(request):
    try:
        store = Store.objects.get(owner=request.user)  # Получаем магазин текущего пользователя
        products = Product.objects.filter(store=store)  # Получаем товары, связанные с магазином
    except Store.DoesNotExist:
        return redirect('create_store')  # Если магазина нет, перенаправляем на создание

    return render(request, 'store/dashboard.html', {
        'store': store,
        'products': products,
    })

# Создание магазина
@login_required
def create_store_view(request):
    try:
        # Проверяем, есть ли уже магазин у пользователя
        existing_store = Store.objects.get(owner=request.user)
        return redirect('store_dashboard')  # Если магазин уже существует, отправляем на дашборд
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


# Добавление товара в магазин
@login_required
def add_product_view(request):
    store = get_object_or_404(Store, owner=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Не забудь request.FILES для загрузки изображений
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('store_dashboard')
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})

# Редактирование товара
@login_required
def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')  # Перенаправляем на панель магазина после редактирования
    else:
        form = ProductForm(instance=product)

    return render(request, 'store/edit_product.html', {'form': form, 'product': product})


# Редактирование магазина
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


# Список всех магазинов
def store_list_view(request):
    stores = Store.objects.all().order_by('-created_at')  # Сортировка по дате создания, начиная с новейших
    return render(request, 'app/store_list.html', {'stores': stores})


@login_required
def add_subcategory_view(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')  # Перенаправление после успешного добавления
    else:
        form = SubCategoryForm()

    return render(request, 'store/add_subcategory.html', {'form': form})



def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('store_dashboard')  # Перенаправление после удаления
