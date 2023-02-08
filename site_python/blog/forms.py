from django import forms 
from .models import Photo, Post


class TitlePhotoForm(forms.ModelForm):
    """Form for image model"""
    required_css_class = 'required'
    photo = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('title', 'photo')



