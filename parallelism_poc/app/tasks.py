import string
import time
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def process_job(job_id):
    print('called-------')
    time.sleep(10)
    return f'Processed job {job_id}'
