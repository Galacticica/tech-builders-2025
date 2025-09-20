"""
File: models.py
Author: Reagan Zierke, Heidi Blank, Lawson Fairchild
Date: 2025-09-19
Description: Model for creations
"""

from django.db import models
from posts.models import Post, Media


class Creation(Post):
    '''
    Creation model extending the base Post model.
    '''
    
    demo = models.URLField(max_length=200, null=True, blank=True)
    area_of_focus = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Creation"
        verbose_name_plural = "Creations"

    def save(self, *args, **kwargs):
        self.post_type = 'creation'
        super().save(*args, **kwargs)