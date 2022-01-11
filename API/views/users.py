from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import (
    UserLoginSerializer,
    UserSerializer,
    UserSignUpSerializer,
)

from ..models import User
from datetime import date, timedelta, datetime

# Serializador general para usuarios
class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    # Acción a realizar, login
    @permission_classes([AllowAny])
    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vals = serializer.save()
        user = User.objects.filter(username=vals["user_data"]["username"])[0]
        print(user)
        token_refresh = vals["refresh"]
        token_access = vals["access"]

        data = {
            "user": UserSerializer(user).data,
            "refresh": token_refresh,
            "access": token_access,
        }

        # Cambia la última vez que inició sesión
        data["user"]["last_login"] = datetime.today()

        # Lee la edad del usuario que inicia sesión con el fin de validar
        # Si ya es mayor de edad en caso de que no lo fuera

        return Response(data, status=status.HTTP_201_CREATED)

    @permission_classes([AllowAny])
    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_201_CREATED)
