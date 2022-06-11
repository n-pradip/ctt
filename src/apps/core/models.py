import hashlib
import random
import string

from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='static/core', max_length=200)
    code = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        getting_file = self.file
        random_string = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        filename = getting_file.name + random_string
        sha_algo = hashlib.sha256(filename.encode())
        unique_code = sha_algo.hexdigest()
        if self.code is None:
            self.code = unique_code
        super(FileModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.file.name
