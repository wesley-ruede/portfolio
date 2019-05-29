from django.shortcuts import render, get_object_or_404 #either get the object or give back a 404 "not found"
from .models import Blog #need to import models

def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blog/allblogs.html', {"blogs":blogs}) #creates functions to return the requested html files

def detail(request, blog_id): #access db with query to blog_id which is an integer 
	detailblog = get_object_or_404(Blog, pk=blog_id) #look up in database if blog_id is a match
	return render(request, 'blog/detail.html', {'blog':detailblog}) #return the request and display detail.html