from rest_framework import serializers

from .models import Character

from accounts.serializer import AccountSerializer


class CharacterSerializer(serializers.ModelSerializer):
    patron = AccountSerializer(read_only=True)

    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = ["gold", "experience", "level"]
        extra_kwargs = {"password": {"write_only": True}}


class CharacterManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class CharacterLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
