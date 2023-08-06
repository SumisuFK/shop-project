from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['size']






class Creationform(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтвердите ваш пароль')
    
class Authform(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')