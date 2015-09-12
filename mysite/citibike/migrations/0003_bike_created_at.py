# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0002_auto_20150911_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 11, 22, 23, 37, 655152), auto_now_add=True),
            preserve_default=False,
        ),
    ]
