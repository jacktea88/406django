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
    # GET http://127.0.0.1:8000/api/books/1/ - 取得特定書籍
    # PUT http://127.0.0.1:8000/api/books/1/ - 更新書籍  
    # DELETE http://127.0.0.1:8000/api/books/1/ - 刪除書籍
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    # GET http://127.0.0.1:8000/api/books/1/reviews/ - 取得書籍評論
    # POST http://127.0.0.1:8000/api/books/1/reviews/ - 新增評論
    # DELETE http://127.0.0.1:8000/api/books/1/reviews/ - 刪除評論
    path('books/<int:book_id>/reviews/', views.book_reviews, name='book_reviews'),
    # GET http://127.0.0.1:8000/api/categories/ - 取得所有分類
    path('categories/', views.categories_list, name='categories_list'),
    # GET http://127.0.0.1:8000/api/categories/1/ - 取得特定分類
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),

    
]