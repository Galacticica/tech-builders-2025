"""
File: models.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Models for forum interactions, including message posting.
"""



from django.db import models

from django.db import models
from accounts.models import User

class Message(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.author} - {self.timestamp}"
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    def get_replies(self):
        return self.replies.all()
    def get_parent(self):
        return self.parent