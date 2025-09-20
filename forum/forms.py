"""
File: forms.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Forms for forum interactions, including message posting.
"""



from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write your message here...', 'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'body': 'Your Reply',
        }