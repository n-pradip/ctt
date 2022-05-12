from django.db import models
from src.apps.core.utils import CodeGenerator

class FileModel(models.Model):
    file = models.FileField(upload_to='static/core', max_length=200)
    # code = models.CharField(default=CodeGenerator(),max_length=128,null=False,blank=False)

    def __str__(self):
        return self.file
