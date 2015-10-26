# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0005_auto_20150915_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='station',
            field=models.ForeignKey(to='citibike.Station', related_name='bikes'),
        ),
    ]
