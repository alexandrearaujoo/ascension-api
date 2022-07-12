from rest_framework import serializers

from .models import Character

from accounts.serializer import AccountSerializer


class CharacterCreationSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    vocation = VocationSerializer()

    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = [
            "gold",
            "experience",
            "level",
            "strength",
            "intellect",
            "agility",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class CharacterUpdateSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    vocation = VocationSerializer(read_only=True)

    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = [
            "gold",
            "experience",
            "level",
            "strength",
            "intellect",
            "agility",
        ]
        extra_kwargs = {"password": {"write_only": True}}
