from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsOwner
from ads.serializers import SelectionSerializer, SelectionCreateSerializer


class SelectionViewSet(ModelViewSet):
    serializer_class = SelectionSerializer
    queryset = Selection.objects.all()

    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwner],
        'partial_update': [IsAuthenticated, IsOwner],
        "destroy": [IsAuthenticated, IsOwner]
    }

    default_serializer = SelectionSerializer
    serializers = {"create": SelectionCreateSerializer,
                   }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
