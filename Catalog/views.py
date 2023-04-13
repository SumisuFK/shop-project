from django.shortcuts import render, redirect
from .forms import Creationform
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(request):
    return render(request,'catalog/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'catalog/signupuser.html', {'form': Creationform()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'catalog/signupuser.html', {'form': Creationform, 'error': 'Данный логин уже используется,выберите другой.'})
        else:
            return render(request, 'catalog/signupuser.html', {'form': Creationform, 'error': 'Пароли не совпадают'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')