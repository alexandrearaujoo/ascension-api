from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdmin, isAccountOwner
from .serializer import CharacterCreationSerializer, CharacterUpdateSerializer
from .models import Character


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
