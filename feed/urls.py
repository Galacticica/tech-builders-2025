"""
File: urls.py
Author: Reagan Zierke
Date: 2025-09-19
Description: description
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='main_feed'),
    path('<slug:slug>/', views.view_post, name='view_post'),
]