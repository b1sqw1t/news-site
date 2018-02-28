from django.shortcuts import render_to_response, redirect,get_object_or_404
from django.views.generic.base import ContextMixin, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,ProcessFormView, FormView
from django.urls import reverse


from news.forms import NewsForm
from news.models import Newsbase

class category_list(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(category_list,self).get_context_data(**kwargs)
        context['category'] = Newsbase.category
        context['authors'] = Newsbase.authors
        return context




class index_list_Views(ListView,category_list):
    model = Newsbase
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'list'

    def get(self,request,*args,**kwargs):
        try:
            self.category = self.kwargs['category']

        except:
            self.category = None

        return super(index_list_Views,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(index_list_Views,self).get_context_data(**kwargs)
        context['category_now'] = self.category
        context['title'] = 'News_Land - Новостной портал'
        return context

    def get_queryset(self):
        if self.category == None:
            return Newsbase.objects.order_by('-news_date')
        else:
            return Newsbase.objects.filter(news_category=self.category).order_by('-news_date')


class post_Views(DetailView,category_list):
    model = Newsbase
    template_name = 'view.html'
    pk_url_kwarg = 'post'
    context_object_name = 'news_post'

    def get(self,request,*args,**kwargs):
        try:
            self.post = self.request.GET['post']
        except:
            self.post = 1
        self.view = get_object_or_404(Newsbase,pk=self.post)
        self.view.news_views += 1
        self.view.save()
        self.authors = Newsbase.authors
        return super(post_Views,self).get(request,*args,**kwargs)


    def get_context_data(self, **kwargs):
        context = super(post_Views,self).get_context_data(**kwargs)
        context['authors'] = self.authors
        return context

    def get_object(self):
        return get_object_or_404(Newsbase,pk=self.post)



def like(request):
    from .models import Newsbase
    try:
        id = request.GET['post']
        post = Newsbase.objects.get(pk=id)
        post.news_liked += 1
        post.save()

        print(post)
        url = '/post?post=' + str(id)
    except:
        url = '/'
    return redirect(url)


class authors_list_Views(ListView,category_list):
    template_name = 'index.html'
    model = Newsbase

    def get(self,request,*args,**kwargs):
        try:
            self.author_name = self.args[0]
        except:
            self.author_name = None
        return super(authors_list_Views,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(authors_list_Views,self).get_context_data(**kwargs)
        context['author_name'] = self.author_name
        return context

    def get_queryset(self):
        return Newsbase.objects.filter(news_authors = self.author_name).order_by('-news_date')





#
#
# class add_news(TemplateView,category_list):
#     template_name = 'add_news.html'
#     form = None
#     def get(self,request,*args,**kwargs):
#         try:
#             cat = self.args[0]
#         except:
#             pass
#         self.form = NewsForm(initial={'news_category':cat})
#         return super(add_news,self).get(request,*args,**kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(add_news,self).get_context_data(**kwargs)
#         context['form'] = self.form
#         context['btn'] = 'Добавить'
#         context['title'] = 'Добавление Новости'
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.form = NewsForm(request.POST)
#         if self.form.is_valid():
#             self.form.save()
#             self.url = Newsbase.objects.last()
#             return redirect('/post?post='+str(self.url.id))
#         return super(add_news,self).get(request,*args,**kwargs)
#
#
#
# class edit_news(TemplateView,category_list):
#     template_name = 'add_news.html'
#     form = None
#     post_id = None
#
#     def get(self,request,*args,**kwargs):
#         try:
#             self.post_id = self.args[0]
#         except:
#             self.post_id = 1
#         self.form = NewsForm(instance=Newsbase.objects.get(id=self.post_id))
#         return super(edit_news,self).get(request,*args,**kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(edit_news,self).get_context_data(**kwargs)
#         context['post'] = Newsbase.objects.get(id=self.post_id)
#         context['post_id'] = self.post_id
#         context['form'] = self.form
#         context['btn'] = 'Применить'
#         context['title'] = 'Редактирование новости'
#
#         return context
#
#     def post(self,request,*args,**kwargs):
#         self.post_id = self.args[0]
#         post = Newsbase.objects.get(id=self.post_id)
#         self.form = NewsForm(request.POST,instance=post)
#         if self.form.is_valid():
#             print('IS_VALID')
#             self.form.save()
#             print('REDIRECT = '+'/post?=post'+str(self.post_id))
#             return redirect('/post?post='+str(self.post_id))
#         return super(edit_news, self).get(request, *args, **kwargs)



class add_news(TemplateView,category_list):
    form = None
    template_name = 'add_news.html'

    def get(self, request, *args, **kwargs):
        self.form = NewsForm()
        if self.args[0]:
            self.category = self.args[0]
            self.form = NewsForm(initial={'news_category':self.category})


        return super(add_news,self).get(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(add_news,self).get_context_data(**kwargs)
        context['form'] = self.form
        context['btn'] = 'Применить'
        context['title'] = 'Добавление новой новости'
        return context

    def post(self,request,*args,**kwargs):
        self.form = NewsForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect('/')
        return super(add_news,self).get(request,*args,**kwargs)


class edit_news(TemplateView,category_list):
    form = None
    template_name = 'add_news.html'

    def get(self, request, *args, **kwargs):
        if self.args[0]:
            self.post_id = self.args[0]
        try:
            self.news = Newsbase.objects.get(pk=self.post_id)
        except:
            return redirect('/')
        self.form = NewsForm(instance=self.news)

        return super(edit_news, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(edit_news,self).get_context_data(**kwargs)
        context['form'] = self.form
        context['btn'] = 'Применить'
        context['title'] = 'Редактирование новости'
        return context

    def post(self,request,*args,**kwargs):
        self.post_id = self.args[0]
        self.news = Newsbase.objects.get(pk=self.post_id)
        self.form = NewsForm(request.POST, instance=self.news)
        if self.form.is_valid():
            self.form.save()
            return redirect('/post?post='+self.post_id)
        return super(edit_news,self).get(request,*args,**kwargs)


class delete_news(TemplateView):
    def get(self,request,*args,**kwargs):
        self.news = get_object_or_404(Newsbase,pk=self.args[0])
        self.news.delete()
        return redirect('/')

