"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Catalog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),

    #Auth
    # path('signup/', views.signupuser, name='signupuser'),
    # path('logout/', views.logoutuser, name='logoutuser'),
    # path('login/', views.loginuser, name='loginuser'),
    
    #Cart
    path('cart_all/', include('cart.urls', namespace='cart')),

    #Catalog
    
    path('', views.home, name='home'),
    path('product/', include('Catalog.urls')),
    
    #Tech
    path('privacy_policy/', views.privacy_policy, name='policy'),
    path('payment&delivery/', views.delivery, name='delivery'),
    path('refund', views.refund, name='refund'),
    path('public_offer', views.public_offer, name='offer')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)