from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .permissions import ArtisansCustomPermissions
from .serializers import ArtisanSerializer
from .models import Artisan


class ArtisanList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ArtisansCustomPermissions]

    serializer_class = ArtisanSerializer
    queryset = Artisan.objects.all()
