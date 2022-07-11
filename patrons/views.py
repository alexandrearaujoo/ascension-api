from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .permissions import IsAdminOrReadOnly
from .models import Patron
from .serializer import PatronLoginSerializer, PatronSerializer


class ListCreatePatronView(generics.ListCreateAPIView):
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer


class LoginPatronView(APIView):
    def post(self, request):
        serializer = PatronLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        patron = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )


        if patron:
            token, _ = Token.objects.get_or_create(user=patron)

            return Response({"token": token.key})

        return Response(
            {"message": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED
        )
