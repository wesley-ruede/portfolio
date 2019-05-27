from django.shortcuts import render
from .models import Job

def home(request): #imported urls.py
	jobs = Job.objects # access Job model
	return render(request, 'jobs/home.html', {'jobs':jobs}) #return a generated file named home.html + get jobs dictionary