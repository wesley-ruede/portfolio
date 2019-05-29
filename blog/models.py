from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=50, default=None) #default set to None
	pub_date = models.DateTimeField(null=True)
	body = models.TextField(max_length=500, default=None) #default set to None
	image = models.ImageField(upload_to='images/')

	#creating a summary for text.

	def __str__(self): #data model method
		return self.title #set the name of the object to the title in admin

	def summary(self):
		return self.body[:100] #return only the first 100 characters

	def pub_date_pretty(self):
		return self.pub_date.strftime('%m.%d.%Y') #month, day, year