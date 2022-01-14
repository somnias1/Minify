from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIClient


from ..models import Artist, Country


class ArtistTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        Country.objects.create(country_name="Testland")
        Artist.objects.create(
            artist_name="TestMc",
            origin=Country.objects.get(id=1),
            language="Instrumental",
            description="Test artist",
        )

    def test_artist_query(self):
        client = APIClient()
        response = client.get(
            "/API/artists/",
            {},
            format="multipart",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            [
                {
                    "id": 1,
                    "artist_name": "TestMc",
                    "language": "Instrumental",
                    "description": "Test artist",
                    "origin": {
                        "id": 1,
                        "country_name": "Testland",
                        "country_image": None,
                    },
                }
            ],
        )

    def test_user_remove_artist(self):
        client = APIClient()
        response = client.delete(
            "/API/artists/1/",
            {},
            format="multipart",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
