from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .permissions import ArtisansCustomPermissions
from .serializers import ArtisanSerializer
from .models import Artisan

from items.models import Item
from items.serializers import ItemSerializer


class ArtisanListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ArtisansCustomPermissions]

    serializer_class = ArtisanSerializer
    queryset = Artisan.objects.all()


class ArtisanUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ArtisansCustomPermissions]

    serializer_class = ArtisanSerializer
    queryset = Artisan.objects.all()


class ArtisanCreateItem(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ArtisansCustomPermissions]

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def perform_create(self, serializer):
        artisan = Artisan.objects.get(pk=self.kwargs["pk"])

        serializer.save(artisan=artisan)
