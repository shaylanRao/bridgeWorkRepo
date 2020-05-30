from django.conf import settings
from django.db import models
from django.utils import timezone

class article(models.Model): 
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/')
	text = models.TextField()
	location = models.CharField(max_length=200)
	date = models.DateField(default=timezone.now)


class photo(models.Model):
	article = models.IntegerField()
	image = models.ImageField(upload_to='images/')
	date = models.DateTimeField(default=timezone.now)

