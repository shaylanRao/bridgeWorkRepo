from django.urls import path
from . import views


from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('', 					views.get_homepage, 	name='get_homepage'),
    path('post/<int:pk>/', 		views.post_detail, 		name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, 		name='post_edit'),
    path('posts', 				views.post_list, 		name='post_list'),
    path('add', 				views.add_new, 			name='add_new'),
    path('new_article', 		views.new_article, 		name='new_article'),
	path('new_blog_post', 		views.new_blog_post, 	name='new_blog_post'),
	path('post_del/<int:pk>/',	views.post_del,			name='post_del'),
	path('new_photo',			views.new_photo,		name='new_photo'),
	path('gallery/<pk>/',		views.show_gallery,		name='show_gallery'),
	path('gallery', 			views.full_gallery, 	name='show_full_gallery'),
	path('about',				views.show_about,		name='about')
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 