from django.urls import path,include
from rest_framework.routers import DefaultRouter
from src.apps.core.api.v1.views.views import FileView

router = DefaultRouter()

router.register(r'file',FileView)

urlpatterns = router.urls

