from rest_framework import viewsets
from .mixins import GetSerializerClassMixin
from ..models import Artist

from .permissions import IsAdminUserOrReadOnly

from ..serializers import ArtistInfoSerializer, ArtistCreationSerializer


class ArtistViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistCreationSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_action_classes = {
        "list": ArtistInfoSerializer,
    }

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
