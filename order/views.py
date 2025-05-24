from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
from store.models import Product  # Импортируем модель Product

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    for order in orders:
        order.total_price = order.quantity * order.product.price  # Рассчитываем общую стоимость

    # Получаем первый продукт для примера (или настройте логику по вашему усмотрению)
    product = Product.objects.first()

    return render(request, 'order/order_list.html', {'orders': orders, 'product': product})


@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    store = product.store  # Получаем магазин, к которому принадлежит товар
    if request.method == 'POST':
        form = OrderForm(request.POST, store=store)  # Передаем магазин в форму
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.save()
            return redirect('order_success')  # Перенаправление после успешного заказа
    else:
        form = OrderForm(store=store)  # Передаем магазин в форму

    return render(request, 'order/create_order.html', {
        'product': product,
        'order_form': form,
    })


@login_required
def update_order(request, order_id):
    # Получаем заказ текущего пользователя или возвращаем 404
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            # Сохраняем изменения в заказе
            order = form.save(commit=False)
            # Обновляем статус, если он передан в POST-запросе
            new_status = request.POST.get('status')
            if new_status:
                order.status = new_status
            order.save()
            return redirect('order-list')  # Перенаправление на список заказов
    else:
        # Инициализируем форму с текущими данными заказа
        form = OrderForm(instance=order)
    return render(request, 'order/update_order.html', {'form': form, 'order': order})


@login_required
def delete_order(request, order_id):
    # Получаем заказ текущего пользователя или возвращаем 404
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        # Удаляем заказ
        order.delete()
        return redirect('order-list')  # Перенаправление на список заказов
    return render(request, 'order/delete_order.html', {'order': order})

@login_required
def update_status(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()
            return redirect('order-list')  # Перенаправление на список заказов
    return render(request, 'order/update_status.html', {'order': order})


@login_required
def order_success(request):
    return render(request, 'order/order_success.html', {
        'message': 'Ваш заказ успешно оформлен!',
    })