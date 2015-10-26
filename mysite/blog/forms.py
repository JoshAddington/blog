import itertools

from django import forms
from django.utils.text import slugify
from blog.models import Post


class PostForm(forms.ModelForm):
        class Meta:
                model = Post
                fields = ('title', 'text', 'project')
