# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='availableDocks',
            new_name='available_docks',
        ),
    ]
