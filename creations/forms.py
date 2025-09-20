"""
File: forms.py
Author: Heidi Blank
Date: 2025-09-19
Description: Forms for creating and managing creations.
"""

from django import forms

from .models import Creation
from posts.models import Media

class CreationForm(forms.ModelForm):
        
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
        model = Creation
        fields = ['title', 'content', 'demo', 'area_of_focus']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'demo': forms.URLInput(attrs={'class': 'form-control'}),
            'area_of_focus': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
