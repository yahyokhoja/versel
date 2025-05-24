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
    order = None  # Инициализируем переменную для передачи в шаблон
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order-list')  # Перенаправляем на список заказов
    else:
        order_form = OrderForm(initial={'product': product})

    return render(request, 'order/create_order.html', {
        'order_form': order_form,
        'product': product,
        'order': order  # Передаем объект заказа (может быть None)
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
