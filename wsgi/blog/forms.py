import itertools

from django import forms
from django.utils.text import slugify
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
        class Meta:
                model = Post
                fields = ('title', 'text', 'project')

        def save(self, commit=True):
                instance = super(PostForm, self).save(commit=False)

                # truncate slug to allow for digits
                # only allows single digit
                max_length = int(Post._meta.get_field('slug').max_length) - 2
                instance.slug = orig = slugify(instance.title)[:max_length]

                # appends a digit to the end of the slug if it is used
                for x in itertools.count(1):
                        if not Post.objects.filter(slug=instance.slug).exists():
                                break
                        instance.slug = '%s-%d' % (orig, x)

                if commit:
                        instance.save()

                return instance


class CommentForm(forms.ModelForm):
        class Meta:
                model = Comment
                fields = ('author', 'text')
