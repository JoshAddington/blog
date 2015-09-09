# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('name', models.CharField(max_length=128, unique=True)),
                ('availableDocks', models.IntegerField()),
                ('latitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('longitude', models.DecimalField(max_digits=12, decimal_places=9)),
            ],
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='select a task to record', max_length=100, verbose_name='Task Name')),
                ('history', jsonfield.fields.JSONField(help_text='JSON containing the tasks history', default={}, verbose_name='history')),
            ],
            options={
                'verbose_name_plural': 'Task Histories',
                'verbose_name': 'Task History',
            },
        ),
        migrations.CreateModel(
            name='UpdateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
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
