from django.http import Http404, JsonResponse
from django.shortcuts import render


def index_api(request):
    return JsonResponse({"message": "Hello World! in api/views.py"})
    # return render(request, 'index-bak.html')