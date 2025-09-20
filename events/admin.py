from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event

admin.site.register(Event)


