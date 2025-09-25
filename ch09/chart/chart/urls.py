"""
URL configuration for chart project.

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
from mysite import views

# use django auth login setting
admin.site.site_header = '我的網站header'
admin.site.site_title = '我的網站site title'
admin.site.index_title = '後台管理index title'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='index'),
    path('logout/', views.logout, name='logout'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('votes/', views.votes, name='votes'),
    path('plotly/', views.plotly, name='plotly'),
    
    
]
