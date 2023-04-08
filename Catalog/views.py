from django.shortcuts import render, redirect
from .forms import Creationform

def home(request):
    return render(request,'Catalog/home.html')

def signupuser(request):
    if request.method == 'GET':
        return redirect(request, 'Catalog/sugnupuser.html', {'form': Creationform()})