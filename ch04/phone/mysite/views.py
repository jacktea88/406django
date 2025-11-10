import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from mysite.models import Product

# Create your views here.

def about(request):
#     html = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>about</title>
# </head>
# <body>
#     <h2>Somebody</h2><hr>
#     <p>This is the about page</p>
# </body>
# </html>
#     '''
    quotes = ['今日事，今日畢',
            '要怎麼收穫，先那麼栽',
            '知識就是力量',
            '一個人的個性就是他的命運']

    quote = random.choice(quotes)

    # return HttpResponse(html)
    return render(request, 'about.html', locals())

def list(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def detail(request, id):
    try:
        p = Product.objects.get(id=id)
    except Product.DoesNotExist:
        # return HttpResponseNotFound('找不到商品')
        raise Http404('找不到商品')
    return render(request, 'detail.html', locals())