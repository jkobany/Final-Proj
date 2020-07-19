"""Final3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Device import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('devices/', views.devices, name='devices'),
    path('create/', views.createNewDevice, name='create'),
    path('devices/edit/<int:device_id>', views.editDevice, name='edit'),
    path('devices/delete/<int:device_id>', views.deleteDevice, name='delete'),
    path('form/', views.form, name='form'),
]


