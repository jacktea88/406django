from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

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
    <h2>Somebody</h2><hr>
    <p>This is the about page</p>
</body>
</html>
    '''
    # return HttpResponse(html)
    return render(request, 'about.html')