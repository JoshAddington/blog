from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETINGS_MODULE', 'mysite.settings')
from django.conf import settings

# Indicate Celery to use the default Django settings module

app = Celery('mysite')
app.config_from_object('django.conf:settings')
# This line will tell Celery to autodiscover all your tasks.py that
# are in your app folders
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
