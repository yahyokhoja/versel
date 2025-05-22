from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order-list'),  # Список заказов пользователя
    path('create/<int:product_id>/', views.create_order, name='create-order'),  # Создание заказа для продукта
]
