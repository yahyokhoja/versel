from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StoreForm
from .models import Store
from django.shortcuts import render, get_object_or_404
from .models import Store

def store_detail_view(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'store/store_detail.html', {'store': store})


@login_required
def create_store_view(request):
    if hasattr(request.user, 'store'):
        return redirect('store_detail', store_id=request.user.store.id)

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = StoreForm()
    return render(request, 'store/create_store.html', {'form': form})

