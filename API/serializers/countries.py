from rest_framework import serializers
from ..models import Country


class CountryCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name", "country_image"]


class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "country_name", "country_image"]
