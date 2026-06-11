from django.shortcuts import redirect, render
from mysite import models, forms
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

# 一、基本的表單處理

# def index(request):
#     years = range(1912, 2020)
#     # 二、接收表單資料
#     try:
#         user_id = request.GET['user_id']
#         user_pass = request.GET['user_pass']
#         # 三、下拉選單與核取方塊
#         user_byear = request.GET['byear']
#         urfcolor = request.GET.getlist('fcolor')
#     except:
#         user_id = None
#     if user_id == 'admin' and user_pass == '12345678':
#         verified = True
#     else:
#         verified = False
#     # 一、表單簡介：登入
#     return render(request, 'index.html', locals())

# 二、將表單資料寫入資料庫
# copy from 上面的 index() function
# def index(request):
#     # 一、讀取資料庫資料備用
#     posts = models.Post.objects.all().order_by('-pub_time')
#     moods = models.Mood.objects.all()
#     try:
#         user_id = request.GET['user_id']
#         user_pass = request.GET['user_pass']
#         user_post = request.GET['user_post']
#         user_mood = request.GET['mood']
#     except:
#         user_id = None
#         message = '每一欄都要填寫'
    
#     if user_id != None:
    
#         mood = models.Mood.objects.get(status = user_mood)
#         post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
#         # post = models.Post( ,nickname = user_id, message = user_post, del_pass = user_pass)
#         post.save()
#         message = '張貼成功'
#     else:
#         message = '無效的帳號'

#     return render(request, 'index_post.html', locals())

# 三、使用POST方法提交表單資料 (copy from 上面的 index(二) function)
def index(request):
    posts = models.Post.objects.all().order_by('-pub_time')
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        # user_id = request.GET['user_id']
        # user_pass = request.GET['user_pass']
        # user_post = request.GET['user_post']
        # user_mood = request.GET['mood']

        print('by view.index', user_id, user_pass, user_post, user_mood)
    except:
        user_id = None
        message = '每一欄都要填寫by POST except'
    if user_id != None:
        
        mood = models.Mood.objects.get(status = user_mood)
        post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '張貼成功 by POST'
    else:
        message = '每一欄都要填寫 by POST else'
    # print(user_id, user_pass, user_post, user_mood)    
    return render(request, 'index_post.html', locals())

# 四、拆分不同的URL處理不同的表單資料，並跳轉URL
def listing(request):
    posts = models.Post.objects.order_by('-pub_time')
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    print('by view.posting', request.method)
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        # user_id = request.GET['user_id']
        # user_pass = request.GET['user_pass']
        # user_post = request.GET['user_post']
        # user_mood = request.GET['mood']

        print('by view.posting', user_id, user_pass, user_post, user_mood)
    except:
        user_id = None
        message = '每一欄都要填寫view.posting except'
    if user_id != None:
        
        mood = models.Mood.objects.get(status = user_mood)
        post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '張貼成功view.posting'
    else:
        message = '每一欄都要填寫view.posting else'    
    # message = '如要張貼訊息，則每一個欄位都要填...'
    return render(request, "posting.html", locals())

# 五1、使用Django表單類別處理聯絡表單
# def contact(request):
#     form = forms.ContactForm()
#     return render(request, 'contact.html', locals())

# 五2、使用Django表單類別處理聯絡表單
def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            mail_body = '姓名: %s\n城市: %s\n是否在學: %s\n電子郵件: %s\n意見: %s' % (user_name, user_city, user_school, user_email, user_message)
            email = EmailMessage('來自網站的意見', mail_body, settings.EMAIL_HOST_USER, [user_email])
            email.send()
            message = '您的意見已傳送email給我們'
            print(message)
        else:
            message = '請檢查您的輸入'
            print(message)
    else:  # GET
        form = forms.ContactForm()
        message = '如要寫信給管理員，請留下您的聯絡資訊...'
    return render(request, 'contact.html', locals())

# 六、使用ModelForm類別處理表單資料
def post2db(request):
    print('post 2 db method', request.method)
    # 二、接收表單資料
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            message = '張貼成功'
            print('張貼成功')
            # 三、跳轉到列出訊息的URL
            return redirect('/listing/')
        else:
            message = '每一欄都要填寫view.post2db else POST'
            print('not valid')
    else:  # GET
        # 一、建立表單
        post_form = forms.PostForm()
        moods = models.Mood.objects.all()
        message = '每一欄都要填寫view.post2db else GET'
        print('get')
    return render(request, 'post2db.html', locals())