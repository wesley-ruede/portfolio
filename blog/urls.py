#copied from urls.py

from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), #access .views allblogs function 
] #if there is nothing after slash shows allblogs