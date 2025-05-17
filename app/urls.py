from django.urls import path
from . import views
from .views import create_store_view

urlpatterns = [
    path('', views.index, name='index'),
     path('subcategory/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),
     path('store/<int:store_id>/', views.store_detail, name='store_detail'),
     path('create-store/', create_store_view, name='create_store'),
]
