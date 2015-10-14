import itertools

from django import forms
from django.utils.text import slugify
from projects.models import Project


class ProjectForm(forms.ModelForm):

        class Meta:
                model = Project
                fields = ('title', 'content', 'preview', 'code')
