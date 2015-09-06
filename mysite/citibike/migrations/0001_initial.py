# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number_of_bikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('availableDocks', models.IntegerField()),
                ('latitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('longitude', models.DecimalField(max_digits=12, decimal_places=9)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='station',
            field=models.ForeignKey(to='citibike.Station', related_name='bikes'),
        ),
        migrations.AddField(
            model_name='bike',
            name='update',
            field=models.ForeignKey(to='citibike.UpdateTime', related_name='bike_update'),
        ),
    ]
