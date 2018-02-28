from django.db import models


class Newsbase(models.Model):
    class Meta:
        verbose_name = 'Новости'
    authors = (
        ('Mamaev_Oleg','Мамаев Олег'),
        ('Maksimova_Marina','Максимова Марина'),
        ('Doncova_Dariya','Донцова Дарья'),
    )

    category = (
        ('policy', 'Политика'),
        ('society', 'Общество'),
        ('economy', 'Экономика'),
        ('world', 'В мире'),
        ('sport', 'Спорт'),
        ('incedent', 'Происшествия'),
        ('culture', 'Культура'),
        ('tech', 'Технологии'),
        ('science', 'Наука'),
    )
    news_title = models.CharField(max_length=250,verbose_name='Заголовок',unique=True)
    news_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата и время публикации')
    news_text = models.TextField(verbose_name='Текст статьи',unique=True)
    news_liked = models.IntegerField(default=0,verbose_name='Like')
    news_category = models.CharField(max_length=20,choices=category,verbose_name='Категория')
    news_authors = models.CharField(max_length=30,choices=authors, verbose_name='Автор' )
    news_views = models.IntegerField(default=0,verbose_name='Просмотров')

    def __str__(self):
        return 'Статья:%s, Категория: %s,  Автор: %s' %(self.news_title, self.news_category,self.news_authors)
    def __unicode__(self):
        return self.news_authors
