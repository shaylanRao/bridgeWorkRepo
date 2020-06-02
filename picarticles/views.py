from django.shortcuts import render, redirect, get_object_or_404
from .models import article
from main_photos.models import front_images
from django.utils import timezone
from blog.forms import *


def get_homepage(request):
	#img = homearticle.objects.all()
	img = article.objects.filter(date__lte=timezone.now()).order_by('date')
	banner_photos = front_images.objects.all()
	return render(request, 'homepage/homepage.html',{"img":img, "banner_photos": banner_photos})


def new_photo(request):
	if request.method == "POST":
    	#Access page for first time 
		form = add_article_photo_form(request.POST, request.FILES) 
        #construct the post form
		if form.is_valid():
        #if for is valid
			photo = form.save(commit=False)
			photo.save()
            #adds extra data and saves the form
			img = article.objects.filter(date__lte=timezone.now()).order_by('date')
			banner_photos = front_images.objects.all()
			return render(request, 'homepage/homepage.html',{"img":img, "banner_photos": banner_photos})
			#redirects to the post detail on the post just created
	else:
		form = add_article_photo_form()
	return render(request, 'add/new_photo.html', {'form': form})


def show_gallery(request, pk):
	select_article = get_object_or_404(article, pk=pk)
	select_photos = list(photo.objects.filter(article=pk))
	return render(request, 'gallery/gallery.html', {"select_article":select_article, "select_photos":select_photos})


def full_gallery(request):
	all_photos = photo.objects.all()
	return render(request, 'gallery/full_gallery.html', {"all_photos":all_photos})

def show_about(request):
	return render(request, 'about/about.html')
