from django.utils import timezone
from .models import Post
from picarticles.views import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.http import HttpResponse 
from main_photos.models import front_images


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def new_blog_post(request):
    if request.method == "POST":
    	#Access page for first time 
        form = PostForm(request.POST)
        #construct the post form
        if form.is_valid():
        #if for is valid
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #adds extra data and saves the form
            return redirect('blog/post_detail', pk=post.pk)
            #redirects to the post detail on the post just created
    else:
    	#
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog/post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_del(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

#########################################################################################################


def add_new(request):
    return render(request, 'add/add_new.html') 

def new_article(request):
    if request.method == 'POST': 
        form = add_article_form(request.POST, request.FILES) 

        if form.is_valid(): 
            form.save() 
            return redirect('get_homepage') 
    else: 
        form = add_article_form() 
    return render(request, 'add/new_article.html', {'form' : form})


def article_gallery(request):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


