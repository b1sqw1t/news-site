from django import forms

from news.models import Newsbase

choice = Newsbase.category

class NewsForm(forms.ModelForm):

    class Meta:
        model = Newsbase
        fields = 'news_title','news_text','news_category','news_authors','news_pic1','news_pic2','news_pic3','news_pic4','news_pic5'

    news_title = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols': 60,'class': 'special'}),label='Заголовок статьи')
    news_text = forms.CharField(widget=forms.Textarea(attrs={'rows':8,'cols':60 }),label='Текст статьи',)


