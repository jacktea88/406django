from django.shortcuts import render

# Create your views here.
def index(request):
    msg = 'hello world by render function'
    return render(request, 'index.html', {'msg': msg})