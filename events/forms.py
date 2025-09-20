"""
File: forms.py
Author: Heidi Blank
Date: 2025-09-19
Description: Forms for creating and managing events.
"""

from django import forms
from .models import Event
from posts.models import Media

class EventForm(forms.ModelForm):

    MEDIA_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
    ]
    media_url = forms.URLField(
        required=False,
        label="Media URL (Image or Video)",
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    media_type = forms.ChoiceField(
        choices=MEDIA_TYPE_CHOICES,
        required=False,
        label="Media Type",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Event
        fields = ['title', 'content', 'date_of_event', 'location', 'sign_up_link', 'media_url', 'media_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'sign_up_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

