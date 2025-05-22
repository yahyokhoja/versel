from django.shortcuts import render
from store.models import Store

def index(request):
    stores = Store.objects.prefetch_related('products').all()  # Загружаем магазины с их товарами
    return render(request, 'app/index.html', {'stores': stores})
