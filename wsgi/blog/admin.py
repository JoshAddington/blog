from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
        model = Comment
