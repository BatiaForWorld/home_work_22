from django import forms
from tinymce.widgets import TinyMCE
from .models import Blog

class BlogForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview', )
