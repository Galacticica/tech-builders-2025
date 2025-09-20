from django.urls import path, include
from . import views

urlpatterns = [
    path("create_event/", views.create_event, name="create_event"),
]