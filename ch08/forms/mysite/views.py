from django.shortcuts import render

# Create your views here.
def index(request):
    years = range(1912, 2020)
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_byear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')
    except:
        user_id = None
    if user_id == 'admin' and user_pass == '12345678':
        verified = True
    else:
        verified = False
    return render(request, 'index.html', locals())