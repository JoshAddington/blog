from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
        model = Comment


class PostAdmin(admin.ModelAdmin):
        fieldsets = [
                (None, {'fields': ['author', 'title', 'project', 'text']})
        ]
