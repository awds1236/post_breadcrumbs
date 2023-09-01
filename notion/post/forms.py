from django import forms
from .models import Page

class PostForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']
