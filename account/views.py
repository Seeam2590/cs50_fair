from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# The views have been defined below
def signup(request):
    if request.method == 'POST':
        # Making sure the passwords match
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error':'Username has already been taken'})
            # Create a new user only if username is not taken
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect ('home')
        else:
            return render(request, 'account/signup.html', {'error':'Passwords have to match!'})
    else:
        return render(request, 'account/signup.html')

    return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect ('home')
        else:
            # Making sure valid credentials are put
            return render(request, 'account/login.html', {'error':'Please enter valid credentials'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect ('home')
    return render(request, 'account/signup.html')
