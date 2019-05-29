from django.shortcuts import render
from .models import Blog #need to import models

def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blog/allblogs.html', {"blogs":blogs}) #creates functions to return the requested html files
