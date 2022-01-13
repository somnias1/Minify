from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Country
from .permissions import IsAdminUserOrReadOnly
from ..serializers import CountryInfoSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryInfoSerializer
    permission_classes = [IsAdminUserOrReadOnly]
