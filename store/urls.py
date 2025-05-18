from django.urls import path
from . import views
from .views import create_store_view, store_detail_view

urlpatterns = [
   path('create/', create_store_view, name='create_store'),
   path('<int:store_id>/', store_detail_view, name='store_detail'),
]
