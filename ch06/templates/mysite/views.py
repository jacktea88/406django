from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    msg = 'hello world by render function'
    return render(request, 'index.html', {'msg': msg})

def twtv(request, tv_id=0):
    print('tv_id:', tv_id)
    tv_list = [{'name':'公視', 'tvcode':'4RoJ8pxQWTk'},
        {'name':'非凡', 'tvcode':'pDvz-qnGhWI'},
        {'name':'民視', 'tvcode':'ylYJSBUgaMA'},
        {'name':'中視', 'tvcode':'TCnaIE_SAtM'},]
    tv = tv_list[tv_id]

    now = datetime.now()
    hour = now.hour

    return render(request, 'twtv.html', locals())

def engtv(request, tv_id=0):
    print('tv_id:', tv_id)
    tv_list = [{'name':'Discovery', 'tvcode':'4RoJ8pxQWTk'},
        {'name':'Discovery', 'tvcode':'pDvz-qnGhWI'},
        {'name':'Discovery', 'tvcode':'ylYJSBUgaMA'},
        {'name':'Discovery', 'tvcode':'TCnaIE_SAtM'},]
    tv = tv_list[tv_id]

    return render(request, 'engtv.html', locals())

def carlist(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
    car_list = [ [],
            ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
            ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
            ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
            ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
            ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
              ]
    maker = maker #maker範圍是 0~5
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())