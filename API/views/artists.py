from rest_framework import viewsets

from ..models import Artist

from ..serializers import ArtistInfoSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistInfoSerializer
