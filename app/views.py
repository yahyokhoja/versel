from django.shortcuts import render
from store.models import Store

def index(request):
    stores = Store.objects.all().order_by('-created_at')  # Сортировка магазинов по дате создания
    return render(request, 'app/index.html', {'stores': stores})
