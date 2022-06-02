from rest_framework import serializers

from src.apps.core.models import FileModel
from src.apps.core.utils import CodeGenerator


class FileSerializer(serializers.ModelSerializer):
    code = CodeGenerator

    class Meta:
        model = FileModel
        fields = ['id', 'file', 'code']
