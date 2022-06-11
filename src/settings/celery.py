from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.base')

app = Celery('src')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kathmandu')
app.config_from_object(settings, namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {
    'object-deleter-in-every-30-min': {
        'task': 'src.apps.core.tasks.object_deleter',
        'schedule': crontab(minute="*/1")
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
