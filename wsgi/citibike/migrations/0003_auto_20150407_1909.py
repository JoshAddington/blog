# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0002_auto_20150404_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatetime',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
