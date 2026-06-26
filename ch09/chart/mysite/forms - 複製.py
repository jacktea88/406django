from django import forms
from captcha.fields import CaptchaField
from mysite import models


class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=20)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())

class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label="姓名", max_length=100)
    user_email = forms.EmailField(label="電子郵件")
    user_message = forms.CharField(label="訊息", widget=forms.Textarea)
    user_city = forms.ChoiceField(label="居住城市", choices=CITY)
    # user_city = forms.ChoiceField(label="居住城市", choices=[
    #     ("Taipei", "台北"),
    #     ("Kaohsiung", "高雄"),
    #     ("Taichung", "台中")
    # ])
    captcha = CaptchaField(label="驗證碼")

class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '你的暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'
        self.fields['captcha'].label = '確定你不是機器人'