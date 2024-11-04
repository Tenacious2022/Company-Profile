"""
URL configuration for Ketelopele project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.aboutUs, name='about'),
    path('services/', views.services, name='services'),
    path('industries/', views.industry, name='industry'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'), 
    path('products/premium/', views.premium_view, name='product_premium'),
    path('products/cctv/', views.cctv_view, name='product_cctv'),
    path('products/ac/', views.ac_view, name='product_ac'),
    path('products/wifi/', views.wifi_view, name='product_wifi'),
    path('contact/', views.contact_view, name='contact'),
    
]


