from django.db import models
import datetime


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
        date = models.DateField(default=datetime.date.today())


class Bike(models.Model):
        station = models.ForeignKey(Station)
        number_of_bikes = models.IntegerField()
        update = models.ForeignKey(UpdateTime)

        def __str__(self):
                return str(self.id)


