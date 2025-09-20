"""
File: urls.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Main URL configurations for the project.
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('accounts.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),
    path('', include('feed.urls')),
    path('events/', include('events.urls')),
    path('creations/', include('creations.urls')),
    path('community_projects/', include('community_projects.urls')),
]
