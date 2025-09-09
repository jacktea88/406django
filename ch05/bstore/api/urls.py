from django.urls import path,include
from mysite.views import index, index_api
# API功能，注意要加下面from api.views才能使用到api/views.py的index_api(), 否則會用到mysite/views.py
from api import views

urlpatterns = [
    path('', views.index_api, name='index_api'),
    # GET http://127.0.0.1:8000/api/books/ - 取得所有書籍
    # GET http://127.0.0.1:8000/api/books/?category=1 - 取得分類為1的書籍
    # POST http://127.0.0.1:8000/api/books/ - 新增書籍
    path('books/', views.books_list, name='books_list'),
]