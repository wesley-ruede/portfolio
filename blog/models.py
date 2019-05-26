from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=50, default='Enter the Title')
	pub_date = models.DateTimeField(null=True)
	body = models.TextField(max_length=500, default='Enter your blog post')
	image = models.ImageField(upload_to='images/')