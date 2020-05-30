from django import forms
from .models import Post
from main_photos.models import front_images
from picarticles.models import article, photo

class PostForm(forms.ModelForm):
    class Meta:
    	model = Post
    	fields = ('title', 'text')




class upload_image_form(forms.ModelForm): 
    class Meta:
        model = front_images 
        fields = ['title', 'image', 'location', 'date'] 




class add_article_form(forms.ModelForm): 
    class Meta:
        model = article 
        fields = ['title', 'image', 'text', 'location', 'date'] 



class add_article_photo_form(forms.ModelForm): 
    class Meta:
        model = photo
        fields = ['image', 'date', 'article']