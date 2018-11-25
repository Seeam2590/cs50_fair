from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
def allblogs(request):

    Blog = blog.objects
    return render(request, 'blog/allblogs.html', {'blog':Blog})
def experience(request, blog_id):
    experience = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/experience.html', {'blog':experience})

@login_required(login_url='/account/signup')
def write(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['author'] and request.FILES['image']:
            Blog = blog()
            Blog.title = request.POST['title']
            Blog.body = request.POST['body']
            Blog.author = request.POST['author']
            Blog.image = request.FILES['image']
            Blog.pubdate = timezone.datetime.now()
            Blog.save()
            return redirect('/blog/')
        else:
            return render(request, 'blog/write.html', {'error':'All fields are required!'})


    else:

        return render(request, 'blog/write.html')
