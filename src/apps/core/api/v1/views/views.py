from src.apps.core.api.v1.serializers.serializers import FileSerializer
from src.apps.core.models import FileModel

from src.apps.core.mixin.viewsets import CreateRetrieveUpdateDestroyViewSetMixin


class FileView(CreateRetrieveUpdateDestroyViewSetMixin):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'id'
