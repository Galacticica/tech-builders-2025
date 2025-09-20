from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Video, Post

admin.site.register(Video)
admin.site.register(Post)

