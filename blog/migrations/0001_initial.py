# Generated by Django 2.0 on 2018-03-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, unique=True, verbose_name='Заголовок')),
                ('Author', models.CharField(default='None', max_length=50, verbose_name='Автор')),
                ('Text', models.CharField(max_length=500, verbose_name='Текст')),
                ('Datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
