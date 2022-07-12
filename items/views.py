from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import Item
from .serializers import ItemSerializer
from .permissions import ItemsCustomPermissions


class ListItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        route_parameter_gt = self.request.query_params.get("price_gt")
        route_parameter_lt = self.request.query_params.get("price_lt")

        if route_parameter_gt:
            queryset = (
                Item.objects.filter(owner__isnull=True)
                .filter(price__gt=route_parameter_gt)
                .all()
            )

            return queryset

        if route_parameter_lt:
            queryset = (
                Item.objects.filter(owner__isnull=True)
                .filter(price__lt=route_parameter_lt)
                .all()
            )

            return queryset

        return super().get_queryset().filter(owner__isnull=True)


class RetrieveUpdateDestroyItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [ItemsCustomPermissions]
