import datetime

import pytz
from celery import shared_task, Celery

from src.apps.core.models import FileModel

app = Celery('tasks', broker='redis://localhost:6379/0')


@shared_task(bind=True)
def object_deleter(self):
    """
    Compute the FileModel objects which has crossed the time limit of more than half an hour
    """
    old_objects = FileModel.objects.filter(
        created_at__lte=datetime.datetime.now(pytz.UTC) - datetime.timedelta(minutes=1))
    for each in range(len(old_objects)):
        old_objects[each].delete()
    return "Done"
