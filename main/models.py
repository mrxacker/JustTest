from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f'Image for "{self.post.title}"'
    