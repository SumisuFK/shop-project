from django.shortcuts import render, redirect, get_object_or_404
from .forms import Creationform, Authform
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .models import Product
from cart.forms import CartAddProductForm

def home(request):
    products = Product.objects.all()
    return render(request,'catalog/home.html', {'products': products})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/detail.html', {'product': product, 'cart_product_form': cart_product_form})

def delivery(request):
    return render(request, 'catalog/payment&delivery.html')

def privacy_policy(request):
    return render(request, 'catalog/privacy_policy.html')

def refund(request):
    return render(request, 'catalog/refund.html')

def public_offer(request):
    return render(request, 'catalog/public_offer.html')





# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'catalog/signupuser.html', {'form': Creationform()})
#     else:
#         if User.objects.filter(username = request.POST['username']).exists():
#             messages.error(request, 'Пользователь с таким логином уже зарегистрирован.')
#             return redirect('signupuser') 
        
#         elif User.objects.filter(email = request.POST['email']).exists():
#             messages.error(request, 'Пользователь с таким email уже зарегистрирован.')
#             return redirect('signupuser') 
#         else:
#             if request.POST['password1'] == request.POST['password2']:
#                 try:
#                     user = User.objects.create_user(request.POST['username'], request.POST['email'], password = request.POST['password1'])
#                     user.save()
#                     login(request, user)
#                     messages.success(request, 'Вы успешно зарегистрировались')
#                     return redirect('home')
#                 except IntegrityError:
#                     return render(request, 'catalog/signupuser.html', {'form': Creationform, 'error': 'Данный логин уже используется,выберите другой.'})
#             else:
#                 return render(request, 'catalog/signupuser.html', {'form': Creationform, 'error': 'Пароли не совпадают'})

# def loginuser(request):
#     if request.method == 'GET':
#         return render(request, 'catalog/loginuser.html', {'form': Authform()})
#     else:
#         user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
#         if user is None:
#             messages.error(request, 'Пользователь не найден.')
#             return redirect('loginuser')
#         else:
#             login(request, user)
#             return redirect('home')

# def logoutuser(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')