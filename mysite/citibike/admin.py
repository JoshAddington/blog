from django.contrib import admin
from . import models


class TaskHistoryAdminModel(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        models.TaskHistory


class StationAdminModel(admin.ModelAdmin):

    class Meta:
        models.Station


class UpdateTimeAdminModel(admin.ModelAdmin):

    class Meta:
        models.UpdateTime


class BikeAdminModel(admin.ModelAdmin):

    class Meta:
        models.Bike


admin.site.register(models.TaskHistory, TaskHistoryAdminModel)
admin.site.register(models.Station, StationAdminModel)
admin.site.register(models.UpdateTime, UpdateTimeAdminModel)
admin.site.register(models.Bike, BikeAdminModel)
