from django.shortcuts import render, redirect
from .forms import Creationform
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

def home(request):
    return render(request,'catalog/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'catalog/signupuser.html', {'form': Creationform()})
    else:
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Пользователь с таким email уже зарегистрирован')
            return redirect('signupuser') 
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(username = username, email = email ,password = password1)
                    user.save()
                    login(request, user)
                    messages.success(request, 'Вы успешно зарегистрировались')
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'catalog/signupuser.html', {'form': Creationform, 'error': 'Данный логин уже используется,выберите другой.'})
            else:
                return render(request, 'catalog/signupuser.html', {'form': Creationform, 'error': 'Пароли не совпадают'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')