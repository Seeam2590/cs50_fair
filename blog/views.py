from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def allblogs(request):
    query = request.GET.get("q")
    Blog = blog.objects
    # Searching by a querying a keyword in the body of the blog
    if query:
        Blog = blog.objects.filter(body__icontains=query)
    return render(request, 'blog/allblogs.html', {'blog':Blog,'query':query})


def experience(request, blog_id):
    experience = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/experience.html', {'blog':experience})


@login_required(login_url='/account/signup')
def write(request):
    # Writing a new blog and saving it to the database
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
