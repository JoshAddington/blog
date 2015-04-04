from django.contrib import admin
from blog.models import Post, Comment


class CommentInline(admin.TabularInline):
        model = Comment


class PostAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['author', 'title', 'slug', 'project', 'text']}),
            ('Date Information', {'fields': ['created_date', 'published_date']}),
        ]

        list_display = ('title', 'created_date', 'published_date')

        prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['author', 'post', 'text', 'posted_date']}),
        ]

        list_display = ('post', 'author', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
