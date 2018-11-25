
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name ='allblogs'),
    path('write', views.write, name ='write'),
    path('<int:blog_id>', views.experience, name = 'experience')
    ]
