"""
File: forms.py
Author: Heidi Blank
Date: 2025-09-19
Description: Forms for creating and managing community projects.
"""

from django import forms
from .models import CommunityProject
from posts.models import Media

class CommunityProjectForm(forms.ModelForm):
    
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
        model = CommunityProject
        fields = ['title', 'content', 'date_of_event', 'location', 'sign_up_link', 'resources_needed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date_of_event': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'sign_up_link': forms.URLInput(attrs={'class': 'form-control'}),
            'resources_needed': forms.Textarea(attrs={'class': 'form-control'}),
        }
