from django.urls import path, include
from . import views

urlpatterns = [
    path("create_project/", views.create_project, name="create_community_project"),
]