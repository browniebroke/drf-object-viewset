from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Object
from .serializers import ObjectSerializer


class ObjectViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
