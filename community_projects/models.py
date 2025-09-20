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

    class Meta:
        verbose_name = "Community Project"
        verbose_name_plural = "Community Projects"