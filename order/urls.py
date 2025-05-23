from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.order_list, name='order-list'),
    path('create/<int:product_id>/', views.create_order, name='create-order'),
    path('update/<int:order_id>/', views.update_order, name='update-order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete-order'),
]
