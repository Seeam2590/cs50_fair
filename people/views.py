from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import people
from django.utils import timezone


from .models import people

# Create your views here.
def home(request):
    # This is the home page
    People = people.objects
    return render(request, 'people/home.html',{'people':People})


def about(request, people_id):
    # This provides an 'about' page of an individual student
    about = get_object_or_404(people, pk= people_id)
    return render(request, 'people/about.html', {'people':about})


@login_required(login_url='/account/signup')
def make(request):
    # Making a student card and saving it into the database
    if request.method == 'POST':
        if request.POST['name'] and request.POST['about'] and request.POST['house_class'] and request.FILES['image']:
            People = people()
            People.name = request.POST['name']
            People.about = request.POST['about']
            People.house_class = request.POST['house_class']
            People.image = request.FILES['image']
            People.save()
            return redirect('/')
        else:
            return render(request, 'people/make.html', {'error':'All fields are required!'})
    else:
        return render(request, 'people/make.html')
