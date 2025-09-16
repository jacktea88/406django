from django.shortcuts import redirect, render
from mysite import models, forms
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
# def index(request):
#     years = range(1912, 2020)
#     try:
#         user_id = request.GET['user_id']
#         user_pass = request.GET['user_pass']
#         user_byear = request.GET['byear']
#         urfcolor = request.GET.getlist('fcolor')
#     except:
#         user_id = None
#     if user_id == 'admin' and user_pass == '12345678':
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
#     except:
#         # user_id = None
#         message = '每一欄都要填寫'
    
#     # if user_id != None:
#         mood = models.Mood.objects.get(status = user_mood)
#         post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
#         # post = models.Post( ,nickname = user_id, message = user_post, del_pass = user_pass)
#         # post.save()
#         message = '張貼成功'
#     # else:
#         message = '無效的帳號'

#     return render(request, 'index_post.html', locals())

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

        print(user_id, user_pass, user_post, user_mood)
    except:
        user_id = None
        message = '每一欄都要填寫'
    if user_id != None:
        
        mood = models.Mood.objects.get(status = user_mood)
        post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '張貼成功'
    else:
        message = '每一欄都要填寫'
    # print(user_id, user_pass, user_post, user_mood)    
    return render(request, 'index_post.html', locals())

def listing(request):
    posts = models.Post.objects.order_by('-pub_time')
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting(request):
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

        print(user_id, user_pass, user_post, user_mood)
    except:
        user_id = None
        message = '每一欄都要填寫posting except'
    if user_id != None:
        
        mood = models.Mood.objects.get(status = user_mood)
        post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '張貼成功posting'
    else:
        message = '每一欄都要填寫posting else'    
    # message = '如要張貼訊息，則每一個欄位都要填...'
    return render(request, "posting.html", locals())

# def contact(request):
#     form = forms.ContactForm()
#     return render(request, 'contact.html', locals())

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
    return render(request, 'contact.html', locals())

def post2db(request):
    print('post 2 db method', request.method)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            message = '張貼成功'
            print('張貼成功')
            return redirect('/')
        else:
            message = '每一欄都要填寫post'
            print('not valid')
    else:  # GET
        post_form = forms.PostForm()
        moods = models.Mood.objects.all()
        message = '每一欄都要填寫get'
        print('get')
    return render(request, 'post2db.html', locals())