from django.contrib import admin
from .models import Blog_model

class Blog_model_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Author', 'Text', 'Datetime')

admin.site.register(Blog_model,Blog_model_Admin)