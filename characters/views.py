from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdmin, IsAccountOwnerOrReadOnly, isAccountOwner
from .serializer import CharacterLoginSerializer, CharacterSerializer
from .models import Character


class ListCreateUserView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin, isAccountOwner]

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class RetrieveUpdateDeleteCharacterView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAccountOwner]

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class LoginCharacterView(APIView):
    def post(self, request):
        serializer = CharacterLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        character = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if character:
            token, _ = Token.objects.get_or_create(user=character)

            return Response({"token": token.key})

        return Response(
            {"message": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED
        )
