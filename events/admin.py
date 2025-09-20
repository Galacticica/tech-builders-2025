"""
File: admin.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Admin configuration for Event model
"""



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event

admin.site.register(Event)


