from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['author', 'title', 'slug', 'project', 'text']}),
            ('Date Information', {'fields': ['created_date', 'published_date']}),
        ]

        list_display = ('title', 'created_date', 'published_date')

        prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
