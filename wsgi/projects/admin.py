from django.contrib import admin
from projects.models import Project
from blog.models import Post


class LinkInline(admin.TabularInline):
        model = Post.project.through


class ProjectAdmin(admin.ModelAdmin):
        inlines = [LinkInline, ]
        prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)
