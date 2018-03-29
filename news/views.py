from django.shortcuts               import render_to_response, redirect,get_object_or_404,render
from django.contrib                 import messages
from django.contrib.auth            import authenticate,login,logout
from django.contrib.auth.forms      import UserCreationForm
from django.views.generic.list      import ListView
from django.views.generic.base      import ContextMixin, TemplateView
from django.views.generic.detail    import DetailView
from django.views.generic.edit      import CreateView,UpdateView,DeleteView,ProcessFormView, FormView

from news.forms                     import NewsForm, LoginForm,ProfileForm,UserForm,CommentForm
from news.models                    import Newsbase, Testbase, Profile, Comments
from django.contrib.auth.models     import User

class category_list(ContextMixin,LoginForm):
    def get_context_data(self, **kwargs):
        context = super(category_list,self).get_context_data(**kwargs)
        context['category'] = Newsbase.category
        context['authors'] = Newsbase.authors
        context['login_form'] = LoginForm()
        context['top5'] = Newsbase.objects.order_by('-news_liked')[0:5]
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


class ria_list_Views(ListView,category_list):
    model = Testbase
    template_name = 'ria_index.html'
    paginate_by = 5
    context_object_name = 'list'

    def get(self,request,*args,**kwargs):
        try:
            self.category = self.kwargs['category']

        except:
            self.category = None

        return super(ria_list_Views,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(ria_list_Views,self).get_context_data(**kwargs)
        context['category_now'] = self.category
        context['title'] = 'News_Land : РИА - РИА Новости портал'
        return context

    def get_queryset(self):
        if self.category == None:
            return Testbase.objects.order_by('-datetime')
        else:
            #return Newsbase.objects.filter(news_category=self.category).order_by('-news_date')
            return Newsbase.objects.order_by('-datetime')


class post_Views(DetailView,category_list):
    model = Newsbase
    template_name = 'view.html'
    pk_url_kwarg = 'post'
    context_object_name = 'news_post'
    commentForm = None

    def get(self,request,*args,**kwargs):
        try:
            self.post = self.request.GET['post']
        except:
            self.post = 1
        self.view = get_object_or_404(Newsbase,pk=self.post)
        self.commentForm = CommentForm(initial={'comment_news' : self.view,'comment_author': request.user})
        self.comments = Comments.objects.filter(comment_news=self.post)
        self.view.news_views += 1
        self.view.save()
        self.authors = Newsbase.authors
        return super(post_Views,self).get(request,*args,**kwargs)


    def get_context_data(self, **kwargs):
        context = super(post_Views,self).get_context_data(**kwargs)
        context['authors'] = self.authors
        context['commentForm'] = self.commentForm
        context['comments'] = Comments.objects.filter(comment_news=self.post)
        return context

    def post(self,request,*args,**kwargs):
        self.authors = Newsbase.authors
        try:
            self.post = self.request.GET['post']
        except:
            self.post = 1
        self.commentForm = CommentForm(request.POST)
        self.new_comment = self.commentForm.save(commit=False)
        self.new_comment.comment_text = request.POST['comment_text']
        self.new_comment.comment_news = Newsbase.objects.get(pk=self.post)
        self.new_comment.comment_author = request.user
        self.new_comment.save()
        self.commentForm.save_m2m()
        return redirect('/post?post='+self.post)
        return super(post_Views,self).get(request,*args,**kwargs)


    def get_object(self):
        return get_object_or_404(Newsbase,pk=self.post)


class ria_post_Views(DetailView,category_list):
    model = Newsbase
    template_name = 'view.html'
    pk_url_kwarg = 'post'
    context_object_name = 'news_post'

    def get(self,request,*args,**kwargs):
        try:
            self.post = self.request.GET['post']
        except:
            self.post = 1
        self.view = get_object_or_404(Testbase,pk=self.post)
        self.view.news_views += 1
        self.view.save()
        return super(ria_post_Views,self).get(request,*args,**kwargs)


    def get_context_data(self, **kwargs):
        context = super(ria_post_Views,self).get_context_data(**kwargs)
        context['authors'] = self.authors
        return context

    def get_object(self):
        return get_object_or_404(Testbase,pk=self.post)


def like(request):
    from .models import Newsbase

    try:
        id = request.GET['post']
        post = Newsbase.objects.get(pk=id)
        post.news_liked += 1
        post.save()
        messages.add_message(request,messages.SUCCESS,'МЫ РАДЫ ЧТО ВАМ ПОНРАВИЛАСЬ НОВОСТЬ')
        try:
            if request.GET['news']:
                url = '/post?post=' + str(id)
        except:
            if request.GET['home']:
                url = request.GET['home']
                url +='#'+request.GET['id']
    except:
        url = '/'
    return redirect(url)


class authors_list_Views(ListView,category_list):
    template_name = 'index.html'
    model = Newsbase
    paginate_by = 5

    def get(self,request,*args,**kwargs):
        author_name = None
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
        self.form = NewsForm(request.POST,request.FILES)
        if self.form.is_valid():
            self.form.save()
            messages.add_message(request, messages.SUCCESS, 'НОВОСТЬ УСПЕШНО ДОБАВЛЕНА')
            return redirect('/')
        messages.add_message(request,messages.ERROR,'ОШИБКА ПРИ ДОБАВЛЕНИИ НОВОСТИ')
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
        self.form = NewsForm(request.POST, request.FILES, instance=self.news)
        if self.form.is_valid():
            self.form.save()
            messages.add_message(request, messages.SUCCESS, 'НОВОСТЬ УСПЕШНО ОТРЕДАКТИРОВАНА')
            return redirect('/post?post='+self.post_id)
        messages.add_message(request,messages.ERROR,'ОШИБКА. НОВОСТЬ НЕ ИЗМЕНЕНА')
        return super(edit_news,self).get(request,*args,**kwargs)


class delete_news(TemplateView):
    def get(self,request,*args,**kwargs):
        try:
            self.news = get_object_or_404(Newsbase,pk=self.args[0])
            self.news.delete()
            messages.add_message(request,messages.SUCCESS,'НОВОСТЬ УСПЕШНО УДАЛЕНА')
            return redirect('/')
        except:
            messages.add_message(request, messages.WARNING, 'ОШИБКА. Возможно вы пытаетесь удалить несуществующую новость')
            return redirect('/')




def test(request):
    from news.models import Testbase
    print('WORK')
    if request.method == 'GET':
        print('РАБОТАЕТ')
        from news import parsing
        context = parsing.main()
        for i in context:
            try:
                p = Testbase(title=i['title'], text=i['text'])
                    # datetime='2006-10-25 14:30',
                    # image='http://yandex.ru',
                    # cop_url='http://google.com')
                p.save()
                print('ГОТОВО')
            except:
                print('ОШИБКА')
                print(i)

    return render_to_response(template_name='test.html', context=locals())


class LoginView(TemplateView,category_list):
    form = None
    template_name = 'registration/login.html'

    def get(self,request,*args,**kwargs):
        self.form = LoginForm()
        return super(LoginView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginView,self).get_context_data(**kwargs)
        context['form'] = self.form

        return context

    def post(self,request,*args,**kwargs):
        self.form = LoginForm(request.POST)
        if self.form.is_valid():
            user = authenticate(username = self.form.cleaned_data['username'],
                             password = self.form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
                else:
                    return super(LoginView,self).get(request,*args,**kwargs)
            else:
                return super(LoginView, self).get(request, *args, **kwargs)
        else:
            return super(LoginView, self).get(request, *args, **kwargs)

class RegisterView(TemplateView,category_list,UserCreationForm):
    form = None
    template_name = 'registration/register.html'

    def get(self,request,*args,**kwargs):
        self.form = UserCreationForm

        return super(RegisterView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegisterView,self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form =UserCreationForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            user = authenticate(username=self.form.cleaned_data['username'],
                                password=self.form.cleaned_data['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('register_step2')
            return redirect('login')
        else:
            return super(RegisterView, self).get(request, *args, **kwargs)

class Step2(TemplateView,category_list):
    template_name = 'registration/steptwo.html'
    form = None
    button = 'Сохранить'
    title = 'Редактирование данных пользователя'

    def get(self,request,*args,**kwargs):
        try:
            self.form = ProfileForm(instance=Profile.objects.get(pk=self.request.user.id))
        except:
            self.form = ProfileForm()
            print('ОШИБКА.ПОЛЬЗОВАТЕЛЬ НЕ НАЙДЕН')

        return super(Step2,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(Step2,self).get_context_data(**kwargs)
        context['form'] = self.form
        context['button_text'] = self.button
        context['title'] = self.title
        return context

    def post(self,request,*args,**kwargs):
        self.form = Profile.objects.get(pk=self.request.user.id)
        self.form = ProfileForm(request.POST,request.FILES,instance=self.form)
        if self.form.is_valid():
            self.form.save()
        return super(Step2,self).get(request,*args,**kwargs)


class LogoutView(TemplateView,category_list):
    template_name = 'registration/logout.html'
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('/')


def show_profile(request,man):
    category = Newsbase.category
    man = request.GET['man']
    top5 = Newsbase.objects.order_by('-news_liked')[0:5]
    try:
        user_object = User.objects.get(pk=man)
        title = 'Профиль пользователя %s' % user_object
    except:
        pass
    return render(request,'registration/show_profile.html',{'user_object'   : user_object,
                                                            'category'      : category,
                                                            'man'           : man,
                                                            'title'         : title,
                                                            'top5'          : top5})

def users(request):
    category = Newsbase.category
    user_objects = User.objects.all()
    return render(request,'registration/users.html',locals())

def proverkra(request):
    return render(request,'test.html')

class delete_comments(TemplateView):

    def get(self,request,*args,**kwargs):
        try:
            comment_id = self.args[0]
            ahref = self.args[1]
            comment = get_object_or_404(Comments,pk=comment_id)
            comment.delete()
            return redirect('/post?post=%s#viewComment' %ahref)
        except:
            return redirect('/')
