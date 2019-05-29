#copied from urls.py

from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), #access .views allblogs function 
    path('<int:blog_id>/', views.detail, name='detail'), #if the user puts in an integer say 1 after blogs/ the request is sent to views
] #if there is nothing after slash shows allblogs