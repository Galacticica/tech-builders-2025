"""
File: models.py
Author: Lawson Fairchild, Reagan Zierke, Heidi Blank
Date: 2025-09-19
Description: Overarching Post model, along with optional Video model.
"""

from django.db import models
from accounts.models import User

class Media(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=500)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='media', null=True, blank=True)

    def __str__(self):
        return self.title

    
class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=50, default='na')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
