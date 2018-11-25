from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import idea
from django.utils import timezone

# Create your views here.
@login_required(login_url='/account/signup')
def allideas(request):
    Ideas = idea.objects.order_by('-votes_total')
    return render(request, 'idea/allideas.html', {'Ideas':Ideas})

@login_required(login_url='/account/signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            Idea = idea()
            Idea.title = request.POST['title']
            Idea.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Idea.body = request.POST['body']
                Idea.url = request.POST['url']
            else:
                Idea.url = 'http://' + request.POST['url']
            Idea.icon = request.FILES['icon']
            Idea.image = request.FILES['image']
            Idea.pubdate = timezone.datetime.now()
            Idea.hunter = request.user
            Idea.save()
            return redirect('/idea/'+str(Idea.id))
        else:
            return render(request, 'idea/create.html', {'error':'All fields are required!'})


    else:

        return render(request, 'idea/create.html')


def detail(request, idea_id):
    detail = get_object_or_404(idea, pk=idea_id)
    return render(request, 'idea/detail.html', {'idea':detail})

@login_required(login_url='/account/signup')
def upvote(request, idea_id):
    if request.method == 'POST':
        Idea = get_object_or_404(idea, pk=idea_id)
        Idea.votes_total += 1
        Idea.save()
        return redirect('/idea/'+str(Idea.id))
