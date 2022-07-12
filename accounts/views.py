from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .permissions import IsAdminOrReadOnly
from .models import Account
from .serializer import AccountLoginSerializer, AccountSerializer


class CreatePatronView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class ListAccountView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginAccountView(APIView):
    def post(self, request):
        serializer = AccountLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        account = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if account:
            token, _ = Token.objects.get_or_create(user=account)

            return Response({"token": token.key})

        return Response(
            {"message": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED
        )
