from rest_framework import generics
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication

from .permissions import IsAdmin, isAccountOwner, isCharacterOwner
from .serializer import CharacterCreationSerializer, CharacterUpdateSerializer
from .models import Character
from missions.models import Missions


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
    permission_classes = [isCharacterOwner]

    def patch(self, request, character_id, mission_id):
        import ipdb

        # ipdb.set_trace()

        try:
            mission = get_object_or_404(Missions, pk=mission_id)
        except Missions.DoesNotExist:
            return Response({"message": "Mission not found"})

        try:
            character = get_object_or_404(Character, pk=character_id)
        except Character.DoesNotExist:
            return Response({"message": "Character not found"})

        if character.level < mission.level_required:
            return Response({"message": "You are too low level for this mission"})
