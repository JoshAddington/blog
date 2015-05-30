from django.db import models
import datetime


# Create your models here.
class Station(models.Model):
        name = models.CharField(max_length=128, unique=True)
        availableDocks = models.IntegerField()
        latitude = models.DecimalField(max_digits=15, decimal_places=12)
        longitude = models.DecimalField(max_digits=15, decimal_places=12)

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
