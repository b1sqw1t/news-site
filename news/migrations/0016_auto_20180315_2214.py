# Generated by Django 2.0 on 2018-03-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20180315_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
