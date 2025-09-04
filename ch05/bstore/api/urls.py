from django.urls import path,include
from mysite.views import index, index_api
# API功能，注意要加下面from api.views才能使用到api/views.py的index_api(), 否則會用到mysite/views.py
from api.views import index_api

urlpatterns = [
    path('', index_api, name='index_api'),
    # path('books/', include('api.urls')),
]