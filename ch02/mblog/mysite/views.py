import random
from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post, Product
from datetime import datetime
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

def about(request):
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
    <title>product</title>
</head>
<body>
    <table>
    {}
    </table>
</body>
</html>
    '''
    tags = "<tr><td>name</td><td>price</td><td>qty</td></tr>"
    for product in products:
        print('product:', product)
        tags += f"<tr><td>{product.name}</td><td>{product.price}</td><td>{product.qty}</td></tr>"
        # print('tags:', tags)
    html = html.format(tags)
    # html = html.replace("{tags}", tags)

    # print('html:', html)
    return HttpResponse(html)
    # return render(request, 'products.html', locals())
