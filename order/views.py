from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
from store.models import Product  # Импортируем модель Product

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Получаем все заказы текущего пользователя
    return render(request, 'order/order_list.html', {'orders': orders})

@login_required
def create_order(request, product_id):
    product = Product.objects.get(id=product_id)  # Находим продукт по ID
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user  # Присваиваем заказу текущего пользователя
            order.save()
            return redirect('order-list')  # Перенаправляем на страницу с заказами
    else:
        order_form = OrderForm(initial={'product': product})  # Инициализируем форму с продуктом

    return render(request, 'order/create_order.html', {'order_form': order_form, 'product': product})
