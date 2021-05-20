import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parallelism_poc.settings')
app = Celery('parallelism_poc')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# The uppercase name-space means that all Celery configuration options must be specified in uppercase instead of lowercase, and start with CELERY_
# e.g, broker_url setting becomes CELERY_BROKER_URL.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
# Celery will automatically discover tasks from all of your installed apps, following the tasks.py convention
app.autodiscover_tasks()