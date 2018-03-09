# Generated by Django 2.0 on 2018-03-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20180307_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='testbase',
            name='news_views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='testbase',
            name='cop_url',
            field=models.URLField(default='http://ria.ru', verbose_name='Ссылка на статью РИА'),
        ),
        migrations.AlterField(
            model_name='testbase',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='testbase',
            name='image',
            field=models.URLField(default='http://ria.ru', verbose_name='Ссылка на изображение'),
        ),
    ]
