from rest_framework import generics

from .serializers import ArtisanSerializer
from .models import Artisan


class ArtisanList(generics.ListAPIView):
    serializer_class = ArtisanSerializer
    queryset = Artisan.objects.all()