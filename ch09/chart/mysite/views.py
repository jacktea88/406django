from django.shortcuts import redirect, render
from mysite import forms, models

# for session
from django.contrib.sessions.models import Session
from django.contrib import messages

# use django auth登入認證
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme

# for votes
from mysite.models import Vote

# use plotly
from plotly.offline import plot
import plotly.graph_objs as go

# for temperature
from mysite.models import Temperature
import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt    

# Create your views here.
# 一、測試cookie是否啟用
# def index(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         message = 'Cookie 已成功啟用'
#     else:
#         message = 'Cookie 啟用失敗'
#         request.session.set_test_cookie()
#     return render(request, 'index.html', locals())

# 三、使用session檢查username是否存在
# def index(request):
#     if 'username' in request.session:
#         username = request.session['username']
#         print('username:in index', username)
#         # message = '登入成功'
#         messages.info(request, '登入成功')
#     else:
#         username = None
#         print('username不存在')
#         # message = '登入失敗'
#         messages.warning(request, '登入失敗')
#     return render(request, 'index.html', locals())

# 八、use django auth for index
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        print('username:in index', username)
        # message = '登入成功'
        messages.info(request, '登入成功')
    else:
        username = None
        print('username不存在')
        # message = '登入失敗'
        messages.warning(request, 'USER不存在，登入失敗')
    return render(request, 'index.html', locals())

# 二、六、基本登入頁面處理、使用messages來顯示登入狀態
# def login(request):
#     if request.method == 'POST':
#         login_form = forms.LoginForm(request.POST)
#         if login_form.is_valid():
#             login_name=request.POST['username'].strip()
#             login_password=request.POST['password']
#             print('login_name:', login_name)
#             try:
#                 user = models.User.objects.get(name=login_name)
#                 if user.password == login_password:
#                     request.session['username'] = login_name
#                     messages.warning(request, '成功登入了')
#                     return redirect('/')
#                 else:
#                     # message = '密碼錯誤'
#                     messages.warning(request, '密碼錯誤')
#             except:
#                 # message = '找不到使用者'
#                 messages.warning(request, '找不到使用者')
#         else:
#             # message = '請檢查輸入的欄位內容'
#             messages.warning(request, '請檢查輸入的欄位內容')
#     else:   # GET
#         login_form = forms.LoginForm()
#     return render(request, 'login.html', locals())

# 七、use django auth login
def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user) # 建立 session 並儲存用戶資訊
                    messages.warning(request, '成功登入了')
                    # 優先從 POST（若 template 有 hidden next）或 GET 取得 next 參數
                    next_url = request.POST.get('next') or request.GET.get('next') or '/'
                    # 安全檢查 next_url 是否指向本站
                    if url_has_allowed_host_and_scheme(next_url, {request.get_host()}):
                        print('go next_url:', next_url)
                        return redirect(next_url)
                    else:
                        return redirect('/')
                else:
                    messages.warning(request, '帳號尚未啟用')
            else:
                messages.warning(request, '登入失敗')
        else:
            messages.warning(request, '請檢查輸入的欄位內容')
    else:   # GET
        login_form = forms.LoginForm()
        print('request.GET: next=', request.GET.get('next', ''))
        # 將 next 傳給 template（若有 ?next=...）以便在 POST 時保留該參數
        next = request.GET.get('next', '')
    return render(request, 'login.html', locals())

# 四、使用session logout
def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        # del request.session['username']
        print('登出成功')
        # message = '登出成功'
        messages.warning(request, '登出成功')
    return redirect('/')

# 五、user info from session
# def userinfo(request):
#     if 'username' in request.session:
#         username = request.session['username']
#         print('username:in userinfo', username)
#     else:
#         print('username不存在')
#         return redirect('/login/')
#     try:
#         userinfo = models.User.objects.get(name=username)
#     except Exception as e:
#         print(e)
#         pass
#     return render(request, 'userinfo.html', locals())

# 九、use django auth userinfo
@login_required(login_url='/login/') # demo須要先登入，如果未登入則跳轉到/login/頁面
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        print('username:in userinfo', username)
    else:
        print('username不存在')
        return redirect('/login/')
    try:
        user = User.objects.get(username=username)
        # userinfo = User.objects.get(username=username)     # 九、用auth內建的User欄位
        userinfo = models.Profile.objects.get(user=user)    # 十一、用自己擴充的Profile欄位
        
        # userinfo = models.User.objects.get(name=username) # 用自己的User欄位
        
    except Exception as e:
        print(e)
        pass
    return render(request, 'userinfo.html', locals())

# 十、use django auth logout
def logout(request):
    auth.logout(request)
    messages.warning(request, '登出成功')
    return redirect('/')

# votes table
def votes(request):
    data = Vote.objects.all().order_by('name')
    return render(request, 'votes.html', locals())
    # return render(request, 'votes_table.html', locals())

# use plotly
def plotly(request):
    data = Vote.objects.all()
    # data = Vote.objects.all().order_by('name')
    x = [d.votes for d in data]
    y = [d.name for d in data][::-1]
    trace = go.Bar(x=x, y=y, name='2022', orientation='h')
    layout = go.Layout(title='2022年高雄市左楠區市議員選舉得票數',
                       height=500)
    fig = go.Figure(data=[trace], layout=layout)
    plot_div = plot(fig, output_type='div')
    return render(request, 'plotly.html', locals())

# 接收溫度數據並儲存到資料庫
@csrf_exempt
def plotly_api(request):
    #接收前端sendTemperatureToBackend(temperature), 
    # 接收XMLHttpRequest()傳來的資料
    print('request.body:', request.body)
    # print('request.POST:', request.POST)
    # print('request:', request)
    if request.body :
        data = json.loads(request.body.decode('utf-8'))
        print('json data:', data)
        # temperature = int(data['temperature'])
        temperature = data['temperature']
    else : 
        temperature = 0
    print(temperature)
    # 儲存溫度數據到資料庫
    temp = Temperature(temperature=temperature)
    temp.save()
    print('溫度數據已儲存到資料庫')
    return HttpResponse(temperature)
    return render(request, 'mqtt.html', locals())

# 啟動mqtt溫度資料傳送
def mqtt_show(request):
    return render(request, 'mqtt.html', locals())

# 使用plotly來繪製溫度圖表
def plotly_mqtt(request):
    data = Temperature.objects.all().order_by('-id')[:10]
    # data = Temperature.objects.all()
    x = [d.created_at for d in data]
    y = [d.temperature for d in data]
    trace = go.Scatter(x=x, y=y, name='溫度', mode='lines+markers')
    layout = go.Layout(title='溫度數據', height=500)
    fig = go.Figure(data=[trace], layout=layout)
    temp_div = plot(fig, output_type='div')
    return render(request, 'temp.html', locals())