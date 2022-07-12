from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import Item
from .serializers import ItemSerializer
from .permissions import ItemsCustomPermissions


class ListItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RetrieveUpdateDestroyItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [ItemsCustomPermissions]
