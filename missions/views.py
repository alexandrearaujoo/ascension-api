from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from patrons.models import Patron

from .permissions import MissionsCustomPermissions

from missions.serializers import MissionSerializer

from .models import Missions

class ListCreateMissionView(generics.ListCreateAPIView):
    queryset = Missions.objects.all()
    serializer_class = MissionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [MissionsCustomPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UpdateMissionView(generics.RetrieveUpdateAPIView):
    queryset = Missions.objects.all()
    serializer_class = MissionSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [MissionsCustomPermissions]

class ListAnMissionOfAnPatronView(generics.ListAPIView):
    serializer_class = MissionSerializer
    lookup_field = 'created_by_id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [MissionsCustomPermissions]

    def get_queryset(self):
        patron = get_object_or_404(Patron, pk=self.kwargs['created_by_id'])
        
        return Missions.objects.filter(created_by_id=patron.id)
        
