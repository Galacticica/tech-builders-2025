"""
File: models.py
Author: Reagan Zierke, Heidi Blank, Lawson Fairchild
Date: 2025-09-19
Description: Model for creations
"""

from django.db import models
from posts.models import Post

class Creation(Post):
    demo = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Creation"
        verbose_name_plural = "Creations"