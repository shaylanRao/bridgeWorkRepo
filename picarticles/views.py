from django.shortcuts import render
from .models import homearticle
from main_photos.models import front_photos
from django.utils import timezone

def get_homepage(request):
	#img = homearticle.objects.all()
	img = homearticle.objects.filter(date__lte=timezone.now()).order_by('date')
	banner_photos = front_photos.objects.all()
	return render(request, 'blog/homepage.html',{"img":img, "banner_photos": banner_photos})