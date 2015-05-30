# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0003_auto_20150407_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='station',
            field=models.ForeignKey(related_name='bikes', to='citibike.Station'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='update',
            field=models.ForeignKey(related_name='bike_update', to='citibike.UpdateTime'),
        ),
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.DecimalField(max_digits=15, decimal_places=12),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.DecimalField(max_digits=15, decimal_places=12),
        ),
    ]
