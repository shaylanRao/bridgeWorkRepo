from django.shortcuts import render
from .models import front_photos

def frontPhotos(request):
	img = front_photos.objects.all()
	return (img)