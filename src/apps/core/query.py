from datetime import datetime

from src.apps.core.models import FileModel

created_time = datetime.datetime.now() - datetime.timedelta(minutes=1)
old_objects = FileModel.objects.filter(created__lte=created_time)

print(old_objects)