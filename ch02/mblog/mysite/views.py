import random
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from mysite.models import Post, Product
from datetime import datetime
from django.urls import reverse
# Create your views here.

def index(request):
    posts = Post.objects.all()
    now = datetime.now()
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse(posts)
    return render(request, 'index.html', locals())

def showpost(request,slug):
    post = Post.objects.get(slug=slug)
    now = datetime.now()
    return render(request, 'showpost.html', locals())

def mqtt(request):
    return render(request, 'mqtt-dashboard-temp-json.html', locals())

def about(request, title, content):
    print('##### title:', title, 'content:', content, '#####')
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>about</title>
</head>
<body>
    <h1>demo by H1</h1>
    hello world, this is about page demo by ""HttpResponse""
</body>
</html>
    '''
    # return HttpResponse(html)

    # return HttpResponse("Hello, world. You're at the about page.")
    return render(request, 'about_basic.html', locals())

def about_quotes(request):
    quotes = [
        '今日事，今日畢',
        '要怎麼收穫，先那麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運'
        
    ]

    quote = random.choice(quotes)
    return render(request, 'about_quote.html', locals())

def products(request):
    products = Product.objects.all()
    # print('products:', products)
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>product list by HttpResponse</title>
</head>
<body>
    <table>
    {}
    </table>
</body>
</html>
    '''
    tags = "<tr><td>name111</td><td>price</td><td>qty</td></tr>"
    for product in products:
        print('product:', product)
        tags += f"<tr><td>{product.name}</td><td>{product.price}</td><td>{product.qty}</td></tr>"
        # print('tags:', tags)
    html = html.format(tags)
    # html = html.replace("{tags}", tags)

    # print('html:', html)
    return HttpResponse(html)
    # return render(request, 'products.html', locals())

def products_id(request, id=1): # 設定default value，預防網址沒帶id
    try:
        product = Product.objects.get(id=id)
        print(product)
    except Product.DoesNotExist:
        # raise Http404("找不到商品")
        return HttpResponseNotFound('找不到商品')
    
    return render(request, 'products_id.html', locals())

def student(request):
    students = [
    {'id': 1, 'name': '張小明', 'age': 20, 'class': 'A班'},
    {'id': 2, 'name': '李小華', 'age': 19, 'class': 'B班'},
    {'id': 3, 'name': '王小美', 'age': 21, 'class': 'A班'},
    {'id': 4, 'name': '陳小強', 'age': 20, 'class': 'C班'},
]
    print('student path name url:', reverse('student-url'))
    return render(request, 'student.html', locals())

def grade(request):
    student_grades = [
    {'id': 1, 'name': '張小明', 'chinese': 95, 'math': 92, 'english': 98},
    {'id': 2, 'name': '李小華', 'chinese': 90, 'math': 76, 'english': 88},
    {'id': 3, 'name': '王小美', 'chinese': 72, 'english': 85, 'math': 70},
    {'id': 4, 'name': '陳小強', 'chinese': 68, 'math': 65, 'english': 62},
]

    # 計算平均分數 (在template中也可以使用custom filter)
    for student in student_grades:
        total = student['chinese'] + student['math'] + student['english']
        student['average'] = round(total / 3, 1)

    return render(request, 'grade.html', locals())