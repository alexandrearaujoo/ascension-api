from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly

from .serializers import VocationSerializer

from .models import Vocation


class ListCreateVocationView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Vocation.objects.all()
    serializer_class = VocationSerializer


class RetrieveUpdateDestroyVocationView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Vocation.objects.all()
    serializer_class = VocationSerializer
