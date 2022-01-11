from django.test import TestCase

from PIL import Image
import tempfile
import json

from rest_framework.test import APIClient
from rest_framework import status

from ..models import User, Membership

from datetime import date


class UserTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        user = User(email="testing@minify.com", username="testing_minify")
        user.set_password("minifytesting1234")
        user.save()

        membership = Membership(
            cost=100,
            membership_name="Testium",
            membership_description="This is a testing membership",
            duration=100,
        )
        membership.save()

    def test_signup_user(self):
        client = APIClient()
        response = client.post(
            "/API/users/signup/",
            {
                "email": "signup.test@minify.com",
                "password": "rc{4@qHjR>!b`yAV",
                "password_confirmation": "rc{4@qHjR>!b`yAV",
                "birth_date": "1998-01-01",
                "username": "testing1",
            },
            format="multipart",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content),
            {
                "user": {
                    "id": 2,
                    "username": "testing1",
                    "email": "signup.test@minify.com",
                    "signup_date": date.today().strftime("%Y-%m-%d"),
                    "birth_date": "1998-01-01",
                    "membership": 1,
                    "queue": 1,
                },
                "refresh": json.loads(response.content)["refresh"],
                "access": json.loads(response.content)["access"],
            },
        )

    def test_login_user(self):

        client = APIClient()
        response = client.post(
            "/API/users/login/",
            {
                "username": "testing_minify",
                "password": "minifytesting1234",
            },
            format="json",
        )
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)
        self.assertIn("access token", result)
