from django.shortcuts import render
from mysite import models

# Create your views here.
def index(request):
    products = models.Product.objects.all() #多對一的查詢
    
    return render(request, 'index.html', locals())

def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)  #針對此product做一對多的查詢
        print('images:',images)
    except:
        pass
    
    return render(request, 'detail.html', locals())