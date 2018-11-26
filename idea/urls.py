from django.urls import path
from . import views

# Url patters after idea/
urlpatterns = [
    path('', views.allideas, name ='allideas'),
    path('create', views.create, name ='create'),
    path('<int:idea_id>', views.detail, name ='detail'),
    path('<int:idea_id>/upvote', views.upvote, name ='upvote'),
    ]
