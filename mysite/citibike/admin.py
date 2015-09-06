from django.contrib import admin
from . import models


class TaskHistoryAdminModel(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        models.TaskHistory

admin.site.register(models.TaskHistory, TaskHistoryAdminModel)
