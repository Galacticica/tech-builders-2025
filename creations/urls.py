from django.urls import path, include
from . import views

urlpatterns = [
    path("create_creation/", views.create_creation, name="create_creation"),
]