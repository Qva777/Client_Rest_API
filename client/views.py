from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    """Функция возвращает "главную" страницу"""
    return render(request, r'client/index.html')


def sign_up(request):
    """Функция возвращает регистрационную страницу"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'client/sign_up.html', {'form': form})


def about(request):
    """Функция возвращает "про нас" страницу"""
    return render(request, 'client/about.html')


def profile(request):
    """Функция возвращает профиль страницу"""
    return render(request, 'client/profile.html')
