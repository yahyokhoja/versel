from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('subcategory/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),
     path('store/<int:store_id>/', views.store_detail, name='store_detail'),
]
