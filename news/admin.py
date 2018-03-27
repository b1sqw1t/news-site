from django.contrib import admin
from . import models
class NewsbaseAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_category','news_authors','news_date')

class Test_Admin(admin.ModelAdmin):
    list_display = ('title','datetime','text',)#'image','cop_url'

class Profile_Admin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','country')

class Comment_admin(admin.ModelAdmin):
    list_display = ('comment_text','comment_news','comment_author')

admin.site.register(models.Newsbase, NewsbaseAdmin)
admin.site.register(models.Testbase,Test_Admin)
admin.site.register(models.Profile,Profile_Admin)
admin.site.register(models.Comments,Comment_admin)