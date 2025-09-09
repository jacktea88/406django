from django.http import Http404, JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt


BOOKS_DATA = [
    {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450, 'category_id': 1},
    {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520, 'category_id': 1},
    {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380, 'category_id': 2},
    {'id': 4, 'title': '機器學習入門', 'author': '陳小美', 'price': 600, 'category_id': 3},
]

CATEGORIES_DATA = [
    {'id': 1, 'name': 'Programming', 'description': '程式設計相關書籍'},
    {'id': 2, 'name': 'Computer Science', 'description': '計算機科學相關書籍'},
    {'id': 3, 'name': 'Machine Learning', 'description': '機器學習相關書籍'},
]

REVIEWS_DATA = [
    {'id': 1, 'book_id': 1, 'rating': 5, 'comment': '很棒的書！', 'user': '讀者A'},
    {'id': 2, 'book_id': 1, 'rating': 4, 'comment': '內容豐富', 'user': '讀者B'},
    {'id': 3, 'book_id': 2, 'rating': 5, 'comment': 'Django入門首選', 'user': '讀者C'},
]


def index_api(request):
    return JsonResponse({
        "message": "BOOK STORE API",
        "version": 1.0,
        "endpoint": {
            "books": "http://127.0.0.1:8000/api/books/",
        }
        
        })
    # return render(request, 'index-bak.html')

@csrf_exempt
def books_list(request):
    #GET http://127.0.0.1:8000/api/books/?category=1 - 取得分類為1的書籍 
    #POST http://127.0.0.1:8000/api/books/ - 新增書籍
    #{"id": 1, "title": "Python\u7a0b\u5f0f\u8a2d\u8a08", "author": "\u738b\u5c0f\u660e", "price": 900, "category_id": 1}  
    books = BOOKS_DATA.copy()
    # print('request:', request)
    # print('request.method:', request, request.method)
    if request.method == 'GET':
        category = request.GET.get('category')
        search = request.GET.get('search')
        if category:
            print('category:', category)
            try:
                category = int(category)
                books = [book for book in books if book['category_id'] == int(category)]
            except ValueError:
                raise Http404
        
        if search:
            print('search:', search)
            books = [book for book in books if search.lower() in book['title'].lower()]
            print('books:', books)
        
    if request.method == 'POST':
        print('request.POST:', request.POST)
        try:
            data = json.loads(request.body)
            print('data:', data)
            new_book = {
                'id': len(BOOKS_DATA) + 1,
                'title': data['title'],
                'author': data['author'],
                'price': data['price'],
                'category_id': data['category_id']
            }
            BOOKS_DATA.append(new_book)
            return JsonResponse({
                'message': '書籍新增成功',
                'book': new_book
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'message': '請提供正確的JSON格式資料'
            }, status=400)


    return JsonResponse({"books": books})
