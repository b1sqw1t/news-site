from django.shortcuts import render,redirect,get_object_or_404
from .forms import Blog_forms
from .models import Blog_model
# Create your views here.

def index(request):
    blog_objects = Blog_model.objects.order_by('-Datetime')
    return render(request,'home_page.html',{'blog_objects':blog_objects})


def add_blog(request):
    forms = Blog_forms()

    if request.method == 'GET':
        if request.user is not None:
            forms = Blog_forms(initial={'Author': request.user.profile.get_full_name()})

    if request.method == "POST":
        forms = Blog_forms(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/blog/')
    return render(request,'add_blog.html',{'forms':forms})


def edit_blog(request,id):
    forms=None
    message = None
    if id is None:
        return redirect('/')
    else:
        blog = get_object_or_404(Blog_model,pk=id)

    if request.method == 'GET':
        blog = get_object_or_404(Blog_model, pk=id)
        forms = Blog_forms(instance=blog)

    if request.method == 'POST':
        blog = get_object_or_404(Blog_model, pk=id)
        forms = Blog_forms(request.POST, instance=blog)
        if forms.is_valid():
            forms.save()
            message = 'БЛОГ ИЗМЕНЕН'


    return render(request, 'edit_blog.html', {'forms': forms, 'blog':blog,'message':message})