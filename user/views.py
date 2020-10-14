from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm

def redirect_to_login(request):
    if request.user.is_anonymous:
        messages.info(request, 'You must log in to view this page.')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        # messages.success(request, 'You are already logged in.')
        return redirect('index')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user has been created!')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        # messages.info(request, 'You are already logged in.')
        return redirect('index')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            password = data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
        messages.info(request, 'Email address OR password is incorrect')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

@login_required(login_url='redirect_to_login')
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')