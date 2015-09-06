# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('citibike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Task Name', max_length=100, help_text='select a task to record')),
                ('history', jsonfield.fields.JSONField(default={}, verbose_name='history', help_text='JSON containing the tasks history')),
            ],
            options={
                'verbose_name_plural': 'Task Histories',
                'verbose_name': 'Task History',
            },
        ),
    ]
