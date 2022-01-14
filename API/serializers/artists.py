from rest_framework import serializers

from ..models import Artist

from .countries import CountryInfoSerializer


class ArtistCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("artist_name", "language", "description", "origin")

    def create(self, validated_data):
        origin = validated_data.pop("origin")
        instance = super().create({**validated_data, "origin": origin})
        return instance


class ArtistInfoSerializer(serializers.ModelSerializer):
    origin = CountryInfoSerializer(read_only=True)

    class Meta:
        model = Artist
        fields = ("id", "artist_name", "language", "description", "origin")
