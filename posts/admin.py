"""
File: admin.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Admin configuration for Post and Media models
"""



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Media, Post

admin.site.register(Media)
admin.site.register(Post)

