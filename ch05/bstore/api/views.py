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

# ===== 共用的輔助函數 =====
def fine_book_by_id(book_id):
    for book in BOOKS_DATA:
        if book['id'] == book_id:
            return book
    return None

def get_reviews_by_book_id(book_id):
    for review in REVIEWS_DATA:
        if review['book_id'] == book_id:
            return review
    return None

def  find_category_by_id(category_id):
    for category in CATEGORIES_DATA:
        if category['id'] == category_id:
            return category
    return None

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

@csrf_exempt
def book_detail(request, book_id):
    """單本書籍詳細資訊端點
    # GET http://127.0.0.1:8000/api/books/1/ - 取得特定書籍
    # PUT http://127.0.0.1:8000/api/books/1/ - 更新書籍  
    # DELETE http://127.0.0.1:8000/api/books/1/ - 刪除書籍
    """
    book = fine_book_by_id(book_id)
    print('book:', book)
    if not book:
        return JsonResponse({'error': '書籍不存在'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({'book': book})
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            book.update(data)
            return JsonResponse({
                'message': '書籍更新成功',
                'book': book
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'message': '請提供正確的JSON格式資料'
            }, status=400)
    
    elif request.method == 'DELETE':
        BOOKS_DATA.remove(book)
        return JsonResponse({
            'message': '書籍刪除成功'
        })
    
@csrf_exempt
def book_reviews(request, book_id):
    """書籍評論端點
    GET http://127.0.0.1:8000/api/books/1/reviews/ - 取得特定書籍的評論
    POST http://127.0.0.1:8000/api/books/1/reviews/ - 新增特定書籍的評論
    DELETE http://127.0.0.1:8000/api/books/1/reviews/ - 刪除特定書籍的評論
    """
    book = fine_book_by_id(book_id)
    if not book:
            return JsonResponse({'error': '書籍不存在'}, status=404)
        
    if request.method == 'GET':
        reviews = get_reviews_by_book_id(book_id)
        return JsonResponse({
            'book_title': book['title'],
            'reviews': reviews
        })
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_review = {
                'id': len(REVIEWS_DATA) + 1,
                'book_id': book_id,
                'rating': data['rating'],
                'comment': data['comment'],
                'user': data['user']
            }
            REVIEWS_DATA.append(new_review)
            return JsonResponse({
                'message': '評論新增成功',
                'review': new_review
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'message': '請提供正確的JSON格式資料'
            }, status=400)
    elif request.method == 'DELETE':
        reviews = get_reviews_by_book_id(book_id)
        print('REVIEWS_DATA:', REVIEWS_DATA)
        REVIEWS_DATA.remove(reviews)
        return JsonResponse({
            'message': '評論刪除成功'
        })
    else:
        return JsonResponse({'error': '不支援的請求方法'}, status=405)
    

def categories_list(request):
    """分類列表端點
    http://localhost:8000/api/categories/
    """
    return JsonResponse({'categories': CATEGORIES_DATA})

def category_detail(request, category_id):
    """特定分類書籍端點
    http://localhost:8000/api/categories/1/
    """
    category = find_category_by_id(category_id)
    if not category:
        return JsonResponse({'error': 'Category not found'}, status=404)
    
    # 取得該分類的書籍
    books = [book for book in BOOKS_DATA if book['category_id'] == category_id]
    
    return JsonResponse({
        'category': category,
        'books_count': len(books),
        'books': books
    })