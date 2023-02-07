from django import forms 
from .models import Image

class ImageForm(forms.ModelForm):
    """Form for image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')