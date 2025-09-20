"""
File: models.py
Author: Reagan Zierke, Heidi Blank, Lawson Fairchild
Date: 2025-09-19
Description: Model for events
"""

from django.db import models
from posts.models import Post, Media

class Event(Post):
    date_of_event = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    sign_up_link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title or "(No Title)"

    def save(self, *args, **kwargs):
        self.post_type = 'event'
        super().save(*args, **kwargs)