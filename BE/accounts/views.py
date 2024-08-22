from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

from rest_framework import generics
from .models import CustomUser

# Create your views here.

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})
    
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:    # 회원가입 폼 유효 X
            return render(request, 'accounts/signup.html', {'form': form})

    else:
        return render(request, 'accoutns/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'accounts/main.html')
        else:
            error_message = "아이디 또는 비밀번호가 올바르지 않습니다."
            return render(request, 'accounts/login.html', {'error_message': error_message})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def main_view(request):
    return render(request, 'accounts/main.html')