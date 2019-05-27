from django.shortcuts import render

def home(requst): #imported urls.py
	return render(requst, 'jobs/home.html') #return a generated file named home.html