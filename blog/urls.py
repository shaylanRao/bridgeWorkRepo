from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_homepage, name='get_homepage'),
    path('post/<int:pk>/', 		views.post_detail, 		name='post_detail'),
    path('post/new/', 			views.post_new, 		name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, 		name='post_edit'),
    path('posts', 				views.post_list, 		name='post_list'),
]