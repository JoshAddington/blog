# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0004_auto_20150529_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False),
        ),
    ]
