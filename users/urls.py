from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view  # ваша функция регистрации и профиль
from . import views


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', profile_view, name='profile'),  # если есть
    
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    
]
