from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveUpdateDestroyViewSetMixin(mixins.CreateModelMixin,
                                              mixins.RetrieveModelMixin,
                                              mixins.ListModelMixin,
                                              mixins.UpdateModelMixin,
                                              mixins.DestroyModelMixin,
                                              GenericViewSet):
    """
      A viewset that provides `retrieve`, `create`, `update` and
      `destroy` actions.
      To use it, override the class and set the `.queryset` and
      `.serializer_class` attributes.
      """

    pass
