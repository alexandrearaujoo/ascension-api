from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .permissions import MissionsCustomPermissions

from missions.serializers import MissionSerializer

from .models import Missions

class ListCreateMission(generics.ListCreateAPIView):
    queryset = Missions.objects.all()
    serializer_class = MissionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [MissionsCustomPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)