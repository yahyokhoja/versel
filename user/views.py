from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # или другая страница
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'user/profile.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # или куда нужно