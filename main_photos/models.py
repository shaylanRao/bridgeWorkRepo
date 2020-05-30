from django.conf import settings
from django.db import models
from django.utils import timezone


# models.py 
class front_images(models.Model): 
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/') 
	location = models.CharField(max_length=200)
	date = models.DateField(default=timezone.now)

#class all_images(models.Model):
#	article_id = models. 
#	image = models.ImageField(upload_to='images/')
