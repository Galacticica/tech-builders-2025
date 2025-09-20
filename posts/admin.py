from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Media, Post

admin.site.register(Media)
admin.site.register(Post)

