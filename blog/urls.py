"""news_land URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path('^add_blog/$',              views.add_blog,     name='add_blog'),
    re_path('^edit_blog/(\d+)/?$',      views.edit_blog,    name='edit_blog'),
    re_path('',                         views.index,        name='blog_index'),

]
