from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.core.api.v1.serializers.serializers import FileSerializer
from src.apps.core.models import FileModel

from src.apps.core.tasks import object_deleter


class FileUploadView(GenericViewSet, mixins.CreateModelMixin):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'id'


class FileListView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'code'
    filter_fields = ['code', 'id']

    object_deleter.delay()



