from django.contrib         import admin
from django.urls            import path,include,re_path
from django.contrib.auth    import views as auth_views
from news.models            import Newsbase
from news                   import views


urlpatterns = [
    re_path('^test/test$',                  views.test,                             name='test'),
    re_path('^author/(\w+)/?$',             views.authors_list_Views.as_view(),     name='authors'),
    re_path('^post(?:(?P<post>\d+)/)?$',    views.post_Views.as_view(),             name='post'),
    re_path('^like' ,                       views.like,                             name='like'),
    re_path('^(?:(\w+)/)?add_news$',        views.add_news.as_view(),               name='add_news'),
    re_path('^edit/(?:(\d+)/)?$',           views.edit_news.as_view(),              name='edit_news'),
    re_path('^delete/(?:(\d+)/)?$',         views.delete_news.as_view(),            name='delete_news'),
    re_path('^ria/index$',                  views.ria_list_Views.as_view(),         name='ria_index'),
    re_path('^register/$',                  views.RegisterView.as_view(),           name='register'),
    re_path('^register/next_step/$',        views.Step2.as_view(),                  name='register_step2'),
    re_path('^profile(?:(?P<man>\d+)/)?$',  views.show_profile,                     name='show_profile'),
    re_path('^users/$',                     views.users,                            name='users'),
    re_path('^proverkra/$',                 views.proverkra,                        name='proverkra'),
    re_path('^(?:(?P<category>\w+)/)?$',    views.index_list_Views.as_view(),       name='index'),
    re_path('^d_c/(?:(\d+)/)?(?:(\d+)/)?$', views.delete_comments.as_view(),        name='delete_comments')

]
