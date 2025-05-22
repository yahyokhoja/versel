from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from store.models import Store
from .forms import StoreCreateForm

def index(request):
    return render(request, 'app/index.html')  # Указываем путь к вашему шаблону
