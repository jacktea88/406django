from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post
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