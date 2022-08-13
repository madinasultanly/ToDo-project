from ast import Pass
from django.shortcuts import get_object_or_404, render, redirect
from .forms import LoginForm, RegisterForm , ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def profile (request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        username = request.user.username
        user = get_object_or_404(User, username = username)
    #  ilk IKI  SETRIN BASQA vARIANTI  user = get_object_or_404(User, username = request.user.username)
    context = {
        "form": form,
    }
    return render(request, 'profile.html',context)

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        
        login(request, new_user)
        messages.success(request, "Qeydiyyatdan keçdiniz!")
        return redirect('to_do_app:index')

    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form": form,
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
    
        if user is None:
            messages.warning(request, "İstifadəçi adı və ya parol səhvdir")
            return render(request, "login.html", context)

        messages.success(request, "Sayta giriş etdiniz")
        login(request, user)
        return redirect('to_do_app:index')

    return render(request, "login.html", context)
    

def logout_user(request):
    logout(request)
    messages.warning(request, "Saytdan çıxış etdiniz")
    return redirect('to_do_app:index')
    
