# Generated by Django 2.0 on 2018-02-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180227_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsbase',
            name='news_text',
            field=models.TextField(unique=True, verbose_name='Текст статьи'),
        ),
    ]
