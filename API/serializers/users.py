from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import UniqueValidator

from ..models import User

from datetime import date, timedelta


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User

        fields = [
            "id",
            "username",
            "email",
            "signup_date",
            "birth_date",
        ]

    def get_specific_user(self, validate_data):
        infouser = User.objects.filter(username=validate_data)[0]
        return UserSerializer(infouser)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=8, max_length=86)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Credenciales incorrectas")

        self.context["username"] = user
        return data

    def create(self, data):
        refresh = RefreshToken.for_user(user=self.context["username"])
        return {
            "user_data": data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        min_length=8,
        max_length=86,
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    birth_date = serializers.DateField()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate(self, data):
        passwrd = data["password"]
        passwrd_conf = data["password_confirmation"]
        if passwrd != passwrd_conf:
            raise serializers.ValidationError("Password doesn't match")
        password_validation.validate_password(passwrd)
        return data

    def create(self, data):
        data.pop("password_confirmation")
        user = User.objects.create_user(**data, allow_explicit=False)
        return user
