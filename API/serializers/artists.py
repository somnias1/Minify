from rest_framework import serializers

from ..models import Artist


class ArtistCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("artist_name", "language", "description")


class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "artist_name", "language", "description")
