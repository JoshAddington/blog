# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0004_updatetime_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='station_id',
        ),
        migrations.AddField(
            model_name='station',
            name='station_number',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bike',
            name='station',
            field=models.ForeignKey(to_field='station_number', related_name='bikes', to='citibike.Station'),
        ),
    ]
