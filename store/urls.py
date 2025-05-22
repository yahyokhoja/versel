
from django.urls import path
from . import views  # Импортируем views из текущего приложения store
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('subcategory/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),
    path('store/<int:store_id>/', views.store_detail_view, name='store_detail'),
    path('create-store/', views.create_store_view, name='create_store'),
    path('store-dashboard/', views.store_dashboard_view, name='store_dashboard'),
    path('add-product/', views.add_product_view, name='add_product'),
   
    path('edit-product/<int:product_id>/', views.edit_product_view, name='edit_product'),
    path('edit-store/<int:store_id>/', views.edit_store_view, name='edit_store'),
]

# Обслуживаем медиа-файлы в процессе разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
