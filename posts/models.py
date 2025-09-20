"""
File: models.py
Author: Lawson Fairchild, Reagan Zierke, Heidi Blank
Date: 2025-09-19
Description: Overarching Post model, along with optional Video model.
"""

from django.db import models
from accounts.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
