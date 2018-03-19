from django.db import models

# Create your models here.
class Blog_model(models.Model):
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


    Title = models.CharField(max_length=50,verbose_name='Заголовок',unique=True)
    Author = models.CharField(max_length=50,verbose_name='Автор',default='None')
    Text = models.TextField(verbose_name='Текст')
    Datetime = models.DateTimeField(auto_now_add=True,verbose_name='Дата и время')

    def __str__(self):
        return '%s %s %s %s' %(self.Title,self.Author, self.Text, self.Datetime)

    def get_name(self):
        if self.Author == 'None':
            return '%s' %'Аноним'
        else:
            return self.Author

