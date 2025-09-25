from django.shortcuts import redirect, render
from mysite import forms, models
from django.contrib.sessions.models import Session
from django.contrib import messages

# Create your views here.
# def index(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         message = 'Cookie 已成功啟用'
#     else:
#         message = 'Cookie 啟用失敗'
#         request.session.set_test_cookie()
#     return render(request, 'index.html', locals())

# 檢查username是否存在
def index(request):
    if 'username' in request.session:
        username = request.session['username']
        print('username:in index', username)
        # message = '登入成功'
        messages.info(request, '登入成功')
    else:
        username = None
        print('username不存在')
        # message = '登入失敗'
        messages.warning(request, '登入失敗')
    return render(request, 'index.html', locals())

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            print('login_name:', login_name)
            try:
                user = models.User.objects.get(name=login_name)
                if user.password == login_password:
                    request.session['username'] = login_name
                    messages.warning(request, '成功登入了')
                    return redirect('/')
                else:
                    # message = '密碼錯誤'
                    messages.warning(request, '密碼錯誤')
            except:
                # message = '找不到使用者'
                messages.warning(request, '找不到使用者')
        else:
            # message = '請檢查輸入的欄位內容'
            messages.warning(request, '請檢查輸入的欄位內容')
    else:   # GET
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())

# session logout
def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        # del request.session['username']
        print('登出成功')
        # message = '登出成功'
        messages.warning(request, '登出成功')
    return redirect('/')

# user info from session
def userinfo(request):
    if 'username' in request.session:
        username = request.session['username']
        print('username:in userinfo', username)
    else:
        print('username不存在')
        return redirect('/login/')
    try:
        userinfo = models.User.objects.get(name=username)
    except Exception as e:
        print(e)
        pass
    return render(request, 'userinfo.html', locals())
