from rest_framework.routers import DefaultRouter

from src.apps.core.api.v1.views.views import FileUploadView, FileListView

router = DefaultRouter()

router.register(r'uploadfile', FileUploadView, basename='upload_file')
router.register(r'getfile', FileListView, basename='get_file')

urlpatterns = router.urls
