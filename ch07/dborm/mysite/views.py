from django.shortcuts import render
from mysite import models

# Create your views here.
def index(request):
    products = models.Product.objects.all() #多對一的查詢
    
    return render(request, 'index.html', locals())

def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        print('product:', product.price, product.year, product.id)
        # images = models.PPhoto.objects.filter(product=product.id)  #針對此product.id做一對多的查詢
        images = models.PPhoto.objects.filter(product=product)  #.id可省略，因Django會自動使用主鍵查詢
        print('images:',images)
    except:
        pass
    
    return render(request, 'detail.html', locals())