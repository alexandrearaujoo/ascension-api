from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response, status
from .permissions import IsAdmin, isAccountOwner, isRealAccountOwner
from .serializer import CharacterCreationSerializer, CharacterUpdateSerializer
from .models import Character
from missions.models import Missions
import random

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


class PatchMissionCharacterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isRealAccountOwner]

    def patch(self, request, mission_id):
        try:
            mission = get_object_or_404(Missions, pk=mission_id)
        except Missions.DoesNotExist:
            return Response({"message": "Mission not found"})

        try:
            character = get_object_or_404(
                Character, nickname=self.request.data["nickname"]
            )
        except Character.DoesNotExist:
            return Response(
                {"message": "Character not found"}, status.HTTP_404_NOT_FOUND
            )

        if character.level < mission.level_required:
            return Response(
                {"message": "You are too low level for this mission"},
                status.HTTP_406_NOT_ACCEPTABLE,
            )

        if mission in character.missions.all():
            return Response(
                {"message": "You already have this mission"},
                status=status.HTTP_409_CONFLICT,
            )

        success_chance = round(random.random())

        if success_chance >= 0.2:

            character.experience += mission.experience
            character.gold += mission.gold

            while character.experience >= 100:
                character.level += 1
                character.experience -= 100

            character.missions.add(mission)

            character.save()

            character_serializer = CharacterCreationSerializer(
                character, request.data, partial=True
            )

            character_serializer.is_valid()

            response = {
                "message": "Mission succeded",
                "current_level": character_serializer.data["level"],
                "current_gold": character_serializer.data["gold"],
                "current_experience": character_serializer.data["experience"],
            }

            return Response(response)

        response = {"message": "Mission Failed"}

        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


class BuyItemForCharacterView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isRealAccountOwner]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)

        instance = self.get_object()
        character = get_object_or_404(
            Character, nickname=self.request.data["nickname"]
        )

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)

        if character.gold < instance.price:
            return Response(
                {"message": "You don't have gold to buy this item."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if character.level < instance.level_required:
            return Response(
                {"message": "You don't have level enought to buy this item."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if instance.owner is not None:
            return Response(
                {"message": "This item already have an owner."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        item = self.get_object()

        character = Character.objects.get(
            nickname=self.request.data["nickname"]
        )

        character.gold -= item.price
        character.save()
        serializer.save(owner=character)


class ListCharactersAccountView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CharacterUpdateSerializer

    def get_queryset(self):
        return Character.objects.filter(account=self.request.user)
