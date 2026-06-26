from django.shortcuts import render, redirect
from mysite import models
from mysite import forms
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib.sessions.models import Session
from django.contrib import messages

# use django auth登入認證
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# def index(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         print('cookie已啟用已刪除')
#         message = 'cookie已啟用並刪除'
#     else:
#         request.session.set_test_cookie()
#         print('cookie未啟用')
#         message = 'cookie未啟用'
#     return render(request, 'index_post.html')

# def index(request):
#     if 'username' in request.session:
#         username = request.session['username']
#         print('username:in index', username)
#         message = '登入成功'
#         # messages.info(request, '登入成功')
#     else:
#         username = None
#         print('username不存在')
#         message = '登入失敗'
#         # messages.warning(request, 'USER不存在，登入失敗')
#     return render(request, 'index_post.html', locals())

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        print('username:by auth', username)
        message = '登入成功'
        messages.info(request, '登入成功by auth')
    else:
        username = None
        print('username不存在 by auth')
        message = '登入失敗'
        messages.warning(request, 'USER不存在，登入失敗 by auth')
    return render(request, 'index_post.html', locals())

# def login(request):
#     if request.method == 'POST':
#         login_form = forms.LoginForm(request.POST)
#         if login_form.is_valid():
#             login_name = request.POST['username'].strip()
#             login_password = request.POST['password']
#             print('登入成功,login_name:', login_name)
#             messages.info(request, '登入成功')
#             try:
#                 user = models.User.objects.get(name=login_name)
#                 if user.password == login_password:
#                     request.session['username'] = login_name
#                     return redirect('/')
#                 else:
#                     # message = '密碼錯誤'
#                     messages.warning(request, '密碼錯誤')

#             except:
#                 # message = '找不到使用者'
#                 messages.warning(request, '找不到使用者')
#         else:
#             message = '請檢查輸入的欄位內容'
#             messages.warning(request, '請檢查輸入的欄位內容')
#     else:
#         form = forms.LoginForm()

#     return render(request, 'login.html', locals())


def login(request):
    print('auth login:request.method:', request.method)
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user) # 此行建立session並儲存用戶資訊，相當於request.session['username'] = login_name            
                    messages.warning(request, '成功登入了')
                    print('登入成功,login_name:', login_name)
                    # return redirect('/')
                    print('get next?', request.GET.get('next', '/'))
                    # return redirect(request.GET.get('next', '/'))
                else:
                    message = '帳號尚未啟用'
                    messages.warning(request, '帳號尚未啟用')
        else:
            message = '請檢查輸入的欄位內容'
            messages.warning(request, '請檢查輸入的欄位內容')
    else: # GET
        form = forms.LoginForm()

    return render(request, 'login.html', locals())

@login_required(login_url='/login/')
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
        userinfo = User.objects.get(username=username)     # 九、用auth內建的User欄位
        
        # userinfo = models.User.objects.get(name=username) # 用自己建立的User欄位
        
    except Exception as e:
        print(e)
        pass
    return render(request, 'userinfo.html', locals())


# 使用auth內建的登出
def logout(request):
    auth.logout(request)
    return redirect('/')

def vote(request):
    data = models.Vote.objects.all().order_by('name')
    return render(request, 'vote.html', locals())

# def logout(request):
#     if 'username' in request.session:
#         del request.session['username']
#     return redirect('/')

# Create your views here.
# def index(request):
#     years = range(2000, 2010)
#     try:
#         user_id = request.GET['user_id']
#         user_pass = request.GET['user_pass']
#         user_byear = request.GET['byear']
#         urfcolor = request.GET.getlist('fcolor')

#         print(user_id, user_pass, user_byear, urfcolor)
#     except:
#         user_id = None
#     if user_id == 'admin' and user_pass == '1234':
#         verified = True
#     else:
#         verified = False
#     return render(request, 'index.html', locals())

# def index(request):
#     posts = models.Post.objects.all().order_by('-pub_time')
#     moods = models.Mood.objects.all()
#     try:
#         user_id = request.GET['user_id']
#         user_pass = request.GET['user_pass']
#         user_post = request.GET['user_post']
#         user_mood = request.GET['mood']

#         # print(user_id, user_pass, user_post, user_mood)
#         print('mood:from 表單', user_mood)
#     except:
#         user_id = None

#     if user_id != None:
#         mood = models.Mood.objects.get(status = user_mood)
#         print('mood:from db',mood)
#         post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
#         post.save()
#         message = '張貼成功'
#     return render(request, 'index_post.html', locals())

def listing(request):
    # moods = models.Mood.objects.all()
    posts = models.Post.objects.all().order_by('-pub_time')
    return render(request, 'listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        print('in view.posting', user_id, user_pass, user_post, user_mood)
    except:
        user_id = None
        message = '每一欄都要填寫'
    
    if user_id != None:
    
        mood = models.Mood.objects.get(status = user_mood)
        post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '張貼成功'
    else:
        message = '無效的帳號'

    return render(request, 'posting.html', locals())

# def contact(request):
#     form = forms.ContactForm()
#     return render(request, 'contact.html', locals())

def contact(request):
    # form = forms.PostForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print('表單驗證成功')
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            # user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            mail_body = '姓名: %s\n城市: %s\n電子郵件: %s\n意見: %s' % (user_name, user_city, user_email, user_message)
            email = EmailMessage('來自網站的意見', mail_body, user_email, [settings.EMAIL_HOST_USER])
            # email = EmailMessage('來自網站的意見', mail_body, settings.EMAIL_HOST_USER, [user_email])
            print('host email', settings.EMAIL_HOST_USER)
            email.send()
            # form.save()
            message = '表單驗證成功，郵件已發送給您...'
        else:
            message = '表單驗證失敗'
    else: # GET
        form = forms.ContactForm()
        message = '如要寫信給管理員，請留下您的聯絡資訊...'
    return render(request, 'contact.html', locals())

# def post2db(request):
    
#     post_form = forms.PostForm()
#     moods = models.Mood.objects.all()
#     return render(request, 'post2db.html', locals())

def post2db(request):
    
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            print('表單驗證成功')
            post_form.save()
            message = '表單驗證成功，訊息已張貼...'
            return redirect('/listing/')
        else:
            message = '表單驗證失敗'
    else: # GET
        post_form = forms.PostForm()
        moods = models.Mood.objects.all()
        message = '歡迎來到心情留言板，請留下您的心情訊息...'
    return render(request, 'post2db.html', locals())