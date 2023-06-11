from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Creationform(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтвердите ваш пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')