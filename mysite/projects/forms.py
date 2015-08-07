import itertools

from django import forms
from django.utils.text import slugify
from projects.models import Project


class ProjectForm(forms.ModelForm):

        class Meta:
                model = Project
                fields = ('title', 'content', 'preview', 'code')

        def save(self, commit=True):
                instance = super(ProjectForm, self).save(commit=False)

                # truncate slug to allow for digits, if needed
                # only fits singe digit
                max_length = int(Project._meta.get_field('slug').max_length) - 2
                instance.slug = orig = slugify(instance.title)[:max_length]


                # appends digit to slug if it is used
                for x in itertools.count(1):
                        if not Project.objects.filter(slug=instance.slug).exists():
                                break
                        instance.slug = '%s-%d' % (orig, x)

                if commit:
                        instance.save()

                return instance
