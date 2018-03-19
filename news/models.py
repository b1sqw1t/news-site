from django.db                      import models
from django.contrib.auth.models     import User
from django.db.models.signals       import post_save
from django.dispatch                import receiver


class Newsbase(models.Model):

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

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
    news_pic1 = models.ImageField(upload_to='news/pic/%Y/%m/%d',verbose_name='Изображение1')
    news_pic2 = models.ImageField(upload_to='news/pic/%Y/%m/%d',verbose_name='Изображение2',blank=True)
    news_pic3 = models.ImageField(upload_to='news/pic/%Y/%m/%d',verbose_name='Изображение3',blank=True)
    news_pic4 = models.ImageField(upload_to='news/pic/%Y/%m/%d',verbose_name='Изображение4',blank=True)
    news_pic5 = models.ImageField(upload_to='news/pic/%Y/%m/%d',verbose_name='Изображение5',blank=True)

    def __str__(self):
        return 'Статья:%s, Категория: %s,  Автор: %s' %(self.news_title, self.news_category,self.news_authors)

    def __unicode__(self):
        return self.news_authors

    def save(self,*args,**kwargs):
        try:
            this_record = Newsbase.objects.get(id=self.id)
            if this_record.news_pic1 != self.news_pic1:
                this_record.news_pic1.delete(save=False)
        except:
            pass

        try:
            this_record = Newsbase.objects.get(id=self.id)
            if this_record.news_pic2 != self.news_pic2:
                this_record.news_pic2.delete(save=False)
        except:
            pass

        try:
            this_record = Newsbase.objects.get(id=self.id)
            if this_record.news_pic3 != self.news_pic3:
                this_record.news_pic3.delete(save=False)
        except:
            pass

        try:
            this_record = Newsbase.objects.get(id=self.id)
            if this_record.news_pic4 != self.news_pic4:
                this_record.news_pic4.delete(save=False)
        except:
            pass

        try:
            this_record = Newsbase.objects.get(id=self.id)
            if this_record.news_pic5 != self.news_pic5:
                this_record.news_pic5.delete(save=False)
        except:
            pass
        super(Newsbase,self).save(*args,**kwargs)

    def delete(self, *args, **kwargs):
        self.news_pic1.delete(save = False)
        self.news_pic2.delete(save = False)
        self.news_pic3.delete(save = False)
        self.news_pic4.delete(save = False)
        self.news_pic5.delete(save = False)
        super(Newsbase,self).delete(*args,**kwargs)


class Testbase(models.Model):

    class Meta:
        verbose_name = 'Тест риа новости'

    title = models.CharField(max_length=300,verbose_name='Заголовок',unique=True)
    datetime = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Статья')
    image = models.URLField(verbose_name='Ссылка на изображение',default='http://ria.ru')
    cop_url = models.URLField(verbose_name='Ссылка на статью РИА',default='http://ria.ru')
    news_views = models.IntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return '%s %s %s' %(self.title,self.text,self.datetime)


class Profile(models.Model):

    class Meta:
        verbose_name = 'Дополнительная информация профиля'
        verbose_name_plural = 'Дополнительная информация профилей'

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,unique=True,verbose_name='Пользователь')
    first_name = models.CharField(max_length=30,verbose_name='Имя')
    last_name = models.CharField(max_length=30,verbose_name='Фамилия')
    country = models.CharField(max_length=50,verbose_name='Страна')
    my_city = models.CharField(max_length=50,verbose_name='Город')
    age = models.IntegerField(default=0,verbose_name='Возраст')

    def __str__(self):
        return '%s %s %s %s %s %s' %(self.user,self.first_name,self.last_name,self.country,self.my_city,self.age)

    def get_full_name(self):
        return '%s %s' %(self.first_name, self.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()