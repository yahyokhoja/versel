# app/urls.py
# app/urls.py
from django.urls import path
from . import views  # Импортируем views из текущего приложения app
from store.views import create_store_view, store_dashboard_view

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница из app.views
    path('create-store/', create_store_view, name='create_store'),  # Перенаправление на создание магазина
    path('store-dashboard/', store_dashboard_view, name='store_dashboard'),  # Перенаправление на дашборд магазина
    path('about/', views.about_view, name='about'),
]
