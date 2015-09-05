from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
import jsonfield


# Create your models here.
class Station(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=128, unique=True)
        availableDocks = models.IntegerField()
        latitude = models.DecimalField(max_digits=12, decimal_places=9)
        longitude = models.DecimalField(max_digits=12, decimal_places=9)

        def __str__(self):
                return self.name

        def __int__(self):
                return self.id


class UpdateTime(models.Model):
        time = models.TimeField()
        date = models.DateField(default=datetime.date.today)

        def __str__(self):
                return str(self.date + " " + self.time)


class Bike(models.Model):
        station = models.ForeignKey(Station, related_name='bikes')
        number_of_bikes = models.IntegerField()
        update = models.ForeignKey(UpdateTime, related_name='bike_update')

        def __str__(self):
                return str(self.id)


class TaskHistory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Task Name"),
        help_text=_("select a task to record"),
    )
    history = jsonfield.JSONField(
        default={},
        verbose_name=_("history"),
        help_text=_("JSON containing the tasks history")
    )

    class Meta:
        verbose_name = _('Task History')
        verbose_name_plural = _('Task Histories')

        def __str__(self):
            return _("Task History of Task: %s") % self.name
