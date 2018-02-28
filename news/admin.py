from django.contrib import admin
from . import models
class NewsbaseAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_category','news_authors','news_date')
admin.site.register(models.Newsbase,NewsbaseAdmin)

