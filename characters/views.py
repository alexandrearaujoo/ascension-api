from rest_framework import generics
from rest_framework.views import Response, status
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdmin, isAccountOwner, isRealAccountOwner
from .serializer import CharacterCreationSerializer, CharacterUpdateSerializer
from .models import Character

from items.models import Item
from items.serializers import ItemSerializer

class ListCreateUserView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin | isAccountOwner]

    queryset = Character.objects.all()
    serializer_class = CharacterCreationSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class RetrieveUpdateDeleteCharacterView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAccountOwner]

    queryset = Character.objects.all()
    serializer_class = CharacterUpdateSerializer


class BuyItemForCharacterView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isRealAccountOwner]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        instance = self.get_object()
        character = Character.objects.get(username=self.request.data['username'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if character.gold >= instance.price and character.level >= instance.level_required and instance.owner is None:
            self.perform_update(serializer)
        else:
            return Response({"message": "You can't buy this item."}, status=status.HTTP_400_BAD_REQUEST)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        item = self.get_object()
        character = Character.objects.get(username=self.request.data['username'])
        character.gold -= item.price
        character.save()
        serializer.save(owner=character)
        
        