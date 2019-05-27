from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/') #upload image Jobs object
	summary = models.CharField(max_length=200) #name of the image object
	