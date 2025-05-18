from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  # 🔒 Уже вошёл? Иди в профиль

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            login(request, user)

            # 🚀 Редирект по роли
            if user.role == 'store_owner':
                return redirect('create_store')  # или другой URL
            else:
                return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/register.html', {'form': form})



@login_required
def profile_view(request):
    store = getattr(request.user, 'store', None)  # Получаем магазин, если есть
    return render(request, 'user/profile.html', {'store': store})


def logout_view(request):
    logout(request)
    return redirect('home')  # или куда нужно