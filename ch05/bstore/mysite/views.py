from django.http import Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book_list(request):
    # 模擬書籍資料
    books = [
        {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450},
        {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520},
        {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380},
    ]
    
    context = {
        'books': books,
        'page_title': '書籍列表'
    }

    # return JsonResponse(context, status=200)
    return render(request, 'book_list.html', locals())

# 習題二：書籍詳細頁面
MOCK_BOOKS = [
    {
        'id': 1, 'title': 'Python程式設計', 'author': '王小明', 
        'author_slug': 'wang-xiaoming', 'category': 'programming', 
        'price': 450, 'isbn': '978-1-234-56789-0', 'year': 2023
    },
    {
        'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 
        'author_slug': 'li-xiaohua', 'category': 'web-development', 
        'price': 520, 'isbn': '978-1-234-56789-1', 'year': 2024
    },
    {
        'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 
        'author_slug': 'zhang-datong', 'category': 'computer-science', 
        'price': 380, 'isbn': '978-1-234-56789-2', 'year': 2023
    },
    {
        'id': 4, 'title': '機器學習實戰', 'author': '王小明', 
        'author_slug': 'wang-xiaoming', 'category': 'machine-learning', 
        'price': 600, 'isbn': '978-1-234-56789-3', 'year': 2024
    },
]

def book_detail(request, book_id):
    try:
        book = next(book for book in MOCK_BOOKS if book['id'] == book_id)
    except StopIteration:
        raise Http404(f"書籍 ID: {book_id} 的書籍不存在")
    
    context = {
        'book': book,
        'page_title': book['title']
    }
    return render(request, 'book_detail.html', locals())

def books_by_author(request, author_slug):
    filtered_books = [
        book for book in MOCK_BOOKS 
        if book['author_slug'] == author_slug
    ]
    
    if not filtered_books:
        raise Http404(f"作者 '{author_slug}' 不存在或無書籍")
    
    context = {
        'books': filtered_books,
        'author_name': filtered_books[0]['author'],
        'page_title': f'作者：{filtered_books[0]["author"]}'
    }
    return render(request, 'author.html', locals())

def books_by_category(request, category_name):
    filtered_books = []
    for book in MOCK_BOOKS:
        if book['category'] == category_name:
            filtered_books.append(book)
    
    if not filtered_books:
        raise Http404(f"分類 '{category_name}' 不存在或無書籍")
    
    context = {
        'books': filtered_books,
        'category_name': category_name,
        'page_title': f'分類：{category_name}'
    }
    print('filtered_books:', filtered_books)
    return render(request, 'category.html', locals())

def index_api(request):
    return JsonResponse({"message": "Hello World!"})
    # return render(request, 'index_api.html')
