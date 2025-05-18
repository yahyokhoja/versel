

# Create your views here.
# store/views.py
from django.shortcuts import render, redirect
from .forms import StoreForm
from .models import Store
from django.contrib.auth.decorators import login_required

@login_required
def create_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            return redirect('profile')  # после создания → в личный кабинет
    else:
        form = StoreForm()
    return render(request, 'store/create_store.html', {'form': form})
