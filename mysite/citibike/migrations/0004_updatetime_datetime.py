# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0003_bike_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatetime',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
