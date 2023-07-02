from django.contrib import admin
from django.urls import path, include
from Catalog import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:product_id>', views.detail, name='detail'),
]