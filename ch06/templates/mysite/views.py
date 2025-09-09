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

    return render(request, 'twtv.html', locals())

def engtv(request, tv_id=0):
    print('tv_id:', tv_id)
    tv_list = [{'name':'Discovery', 'tvcode':'4RoJ8pxQWTk'},
        {'name':'Discovery', 'tvcode':'pDvz-qnGhWI'},
        {'name':'Discovery', 'tvcode':'ylYJSBUgaMA'},
        {'name':'Discovery', 'tvcode':'TCnaIE_SAtM'},]
    tv = tv_list[tv_id]

    return render(request, 'engtv.html', locals())