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
from django.urls import include, path
from mysite.views import index, showpost,mqtt, about, about_quotes, products, products_id
#習題
from mysite.views import student, grade

#注意網址最後要加上/,不然會讀不到
#順序有關係，由上到下

about_patterns = [
    path('about/',about,{'title':'關於我們','content':'這是關於我們的內容'}),
    path('about-qutoes/',about_quotes),
]

book_patterns = [
    path('products/',products),
    path('products/<str:id>',products),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('post/<slug:slug>', showpost),
    path('mqtt/',mqtt),
    path('authors/', include(about_patterns)),
    # path('about/',about,name='about'),
    # path('about-qutoes/',about_quotes),
    path('book/', include(book_patterns)),
    # path('products/',products_id),
    # path('products/<str:id>',products_id),
    path('student/',student,{'age':20}),
    path('grade/',grade),
]
