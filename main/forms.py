from django import forms
from .models import Post, PostImage
from django.forms import modelformset_factory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

# Create a formset for PostImage
PostImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=1)