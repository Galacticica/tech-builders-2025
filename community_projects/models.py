"""
File: models.py
Author: Reagan Zierke, Heidi Blank, Lawson Fairchild
Date: 2025-09-19
Description: Model for community projects
"""

from django.db import models
from posts.models import Post

class CommunityProject(Post):
    date_of_event = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    resources_needed = models.TextField(null=True, blank=True)
    sign_up_link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Community Project"
        verbose_name_plural = "Community Projects"

    def save(self, *args, **kwargs):
        self.post_type = 'community_project'
        super().save(*args, **kwargs)