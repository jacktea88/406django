from django.shortcuts import render

# Create your views here.
def index(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message = 'Cookie 已成功啟用'
    else:
        message = 'Cookie 啟用失敗'
        request.session.set_test_cookie()
    return render(request, 'index.html', locals())
