from django.db import models

class FileModel(models.Model):
    file = models.FileField(upload_to='static/core', max_length=200)

    def __init__(self):
        return self.file
