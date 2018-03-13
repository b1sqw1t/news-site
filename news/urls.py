from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from news.models import Newsbase
from news import views
urlpatterns = [
    re_path('^test/test$', views.test, name='test'),
    re_path('^author/(\w+)/?$', views.authors_list_Views.as_view(), name='authors'),
    re_path('^post(?:(?P<post>\d+)/)?$', views.post_Views.as_view(), name='post'),
    re_path('^like' ,views.like, name='like'),
    re_path('^(?:(\w+)/)?add_news$', views.add_news.as_view(), name='add_news'),
    re_path('^edit/(?:(\d+)/)?$', views.edit_news.as_view(), name='edit_news'),
    re_path('^delete/(?:(\d+)/)?$', views.delete_news.as_view(), name='delete_news'),
    re_path('^ria/index$', views.ria_list_Views.as_view(), name='ria_index'),
    re_path('^login/$', auth_views.login,{'template_name' : 'registration/login.html',
                                          'extra_context':{'category': Newsbase.category}}, name='login'),
    re_path('^logout/$', auth_views.logout,{'template_name' : 'registration/logout.html',
                                            'next_page': '/'} , name='logout'),
    re_path('^(?:(?P<category>\w+)/)?$', views.index_list_Views.as_view(), name='index'),

    #'django.contrib.auth.views.login',{"template_name" : "login.html","extra_context":{'category':Newsbase.category}},name='login' )
]
