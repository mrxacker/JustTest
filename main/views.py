from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import *

def index(request):
    all_p = Post.objects.all()
    return render(request,'index.html', context={'all_p':all_p})

def add(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        images = request.FILES.getlist('images')  # Get the list of uploaded images

        if post_form.is_valid():
            post = post_form.save()
            for image in images:
                PostImage.objects.create(post=post, image=image)
            return redirect('/')  # Replace 'success_url' with your success URL

    else:
        post_form = PostForm()

    return render(request, 'add.html', {'post_form': post_form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    existing_images = PostImage.objects.filter(post=post)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        images = request.FILES.getlist('images')  # Get the list of new uploaded images
        removed_images = request.POST.get('removed_images', '').split(',')
        if post_form.is_valid():
            post = post_form.save()
            
            # Remove deleted images
            for image_id in removed_images:
                if image_id:
                    PostImage.objects.get(id=image_id).delete()
            
            # Add new images
            for image in images:
                PostImage.objects.create(post=post, image=image)
            
            return redirect('/')  # Replace 'success_url' with your success URL

    else:
        post_form = PostForm(instance=post)

    return render(request, 'add.html', {'post_form': post_form, 'existing_images': existing_images})