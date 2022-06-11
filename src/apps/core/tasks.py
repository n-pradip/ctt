import datetime

from celery import shared_task
from src.apps.core.models import FileModel


@shared_task(bind=True)
def object_deleter(self):
    """
    Compute the FileModel objects which has crossed the time limit of more than half an hour
    """
    return "Done"

