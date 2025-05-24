from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from order.models import Order
from cart.models import CartItem  # Предполагается, что у вас есть модель CartItem


def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  # 🔒 Уже вошёл? Иди в профиль

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            login(request, user)

            # 🚀 Редирект по роли
            if user.role == 'store_owner':
                return redirect('create_store')  # или другой URL
            else:
                return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    store = getattr(request.user, 'store', None)  # Получаем магазин, если есть
    orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Получаем заказы пользователя
    cart_items = CartItem.objects.filter(user=request.user)  # Получаем товары из корзины пользователя

    return render(request, 'users/profile.html', {
        'store': store,
        'orders': orders,
        'cart_items': cart_items,
    })


def logout_view(request):
    logout(request)
    return redirect('home')  # или куда нужно

@login_required
def customer_dashboard(request):
    if request.user.role == 'customer':  # Убедитесь, что пользователь — покупатель
        return render(request, 'users/customer_dashboard.html', {})
    else:
        return render(request, '403.html', status=403)  # Возвращаем ошибку доступа