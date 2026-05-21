from django.http import Http404, JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt


# ===== 習題三共用的輔助函數 =====
def find_book_by_id(book_id):
    for book in BOOKS_DATA:
        if book['id'] == book_id:
            return book
    return None

def get_reviews_by_book_id(book_id):
    allreviews = []
    print('REVIEWS_DATA:', REVIEWS_DATA)
    for review in REVIEWS_DATA:
        if review['book_id'] == book_id:
            allreviews.append(review)
            print('allreviews:', allreviews)
    if not allreviews:
        return None
    return allreviews




def  find_category_by_id(category_id):
    for category in CATEGORIES_DATA:
        if category['id'] == category_id:
            return category
    return None

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

@csrf_exempt
def books_list(request):
    books = BOOKS_DATA.copy()
    # 查詢參數
    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            books_category = []
            try:
                category = int(category)
                for book in books:
                    if book['category_id'] == int(category):
                        books_category.append(book)
                books = books_category
            except ValueError:
                raise Http404
        search = request.GET.get('search')
        if search:
            books_search = []
            for book in books:
                if search.lower() in book['title'].lower():
                    books_search.append(book)
            books = books_search
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            price = data.get('price')
            category_id = data.get('category_id')
            if not all([title, author, price, category_id]):
                return JsonResponse({'error': '缺少必要欄位'}, status=400)
            new_book = {
                'id': len(BOOKS_DATA) + 1,
                'title': title,
                'author': author,
                'price': price,
                'category_id': category_id
            }
            BOOKS_DATA.append(new_book)
            return JsonResponse({'message': '書籍新增成功'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': '無效的JSON格式'}, status=400)

    return JsonResponse({'books': books})

@csrf_exempt
def book_detail(request, book_id):
    book = find_book_by_id(book_id)
    if not book:
        return JsonResponse({'error': '書籍不存在'}, status=404)
    if request.method == 'GET':
        return JsonResponse({'book': book})
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            book.update(data)
            return JsonResponse({'message': '書籍更新成功', 'book': book})
        except json.JSONDecodeError:
            return JsonResponse({'error': '無效的JSON格式'}, status=400)
    elif request.method == 'DELETE':
        BOOKS_DATA.remove(book)
        return JsonResponse({'message': '書籍刪除成功'})

def category_detail(request, category_id):
    category = find_category_by_id(category_id)
    if not category:
        return JsonResponse({'error': '分類不存在'}, status=404)
    return JsonResponse({'category': category})

# ===== API首頁列表 =====
def index_api(request):
    return JsonResponse({
        "message": "BOOK STORE API",
        "version": 1.0,
        "endpoint": {
            "books": "http://127.0.0.1:8000/api/books/",
            "categories": "http://127.0.0.1:8000/api/categories/",
            "book": "http://127.0.0.1:8000/api/books/{book_id}/",
            "category": "http://127.0.0.1:8000/api/categories/{category_id}/",
            "reviews": "http://127.0.0.1:8000/api/reviews/",
            "review": "http://127.0.0.1:8000/api/reviews/{review_id}/",
            
        }
        
        })
    # return render(request, 'index-bak.html')
