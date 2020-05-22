from django.conf import settings
from django.db import models
from django.utils import timezone

class homearticle(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	videofile= models.FileField(upload_to='blog/static/images', null=True, verbose_name="")
	location = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)

	
	def ref_loc(self):
		string = str(self.videofile)
		new_string = string.replace("blog","")
		return new_string