import datetime

import pytz
from celery import shared_task, Celery

from src.apps.core.models import FileModel

# app = Celery('tasks', broker='redis://127.0.0.1:6379/0') # keep "127.0.0.1" for localhost and "redis" on docker
TIME_LIMIT_IN_MINUTES = 1


@shared_task(bind=True)
def object_deleter(self):
    """
    Compute the FileModel objects which has crossed the time limit of more than half an hour
    """
    old_objects = FileModel.objects.filter(
        created_at__lte=datetime.datetime.now(pytz.UTC) - datetime.timedelta(minutes=TIME_LIMIT_IN_MINUTES))
    for each in range(len(old_objects)):
        old_objects[each].delete()
    return True
