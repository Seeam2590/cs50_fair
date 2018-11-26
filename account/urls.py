
from django.urls import path
from . import views

# Appropriate urls for path after account/
urlpatterns = [
    path('signup', views.signup, name ='signup'),
    path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    ]
