from django.conf import settings
from django.db import models
from django.utils import timezone

class front_photos(models.Model):
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	videofile= models.FileField(upload_to='blog/static/images/front_photos', null=True, verbose_name="")
	date = models.DateTimeField(default=timezone.now)
	
	def ref_loc(self):
		string = str(self.videofile)
		new_string = string.replace("blog","")
		return new_string