"""
URL configuration for mblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mysite.views import index, showpost,mqtt, about, about_quotes, products, products_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('post/<slug:slug>', showpost),
    path('mqtt/',mqtt),
    path('about/',about),
    path('about-qutoes/',about_quotes),
    path('products/',products),
    path('products/<str:id>',products_id),
]
