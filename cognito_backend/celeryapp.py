from __future__ import absolute_import
import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cognito_backend.settings')
from django.conf import settings

app = Celery('cognito_backend')
# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace="CELERY")

print(settings.INSTALLED_APPS)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))