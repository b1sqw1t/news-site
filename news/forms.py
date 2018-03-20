from django                         import forms
from django.contrib.auth.models     import User
from news.models                    import Newsbase,Profile

choice = Newsbase.category

class NewsForm(forms.ModelForm):

    class Meta:
        model = Newsbase
        fields = 'news_title','news_text','news_category','news_authors','news_pic1','news_pic2','news_pic3','news_pic4','news_pic5'

    news_title = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols': 60,'class': 'special'}),label='Заголовок статьи')
    news_text = forms.CharField(widget=forms.Textarea(attrs={'rows':8,'cols':60 }),label='Текст статьи',)


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'country','my_city','age')