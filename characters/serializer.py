from asyncore import read
from rest_framework import serializers

from vocations.serializers import VocationSerializer

from .models import Character

from missions.serializers import MissionSerializer

from accounts.serializer import AccountSerializer

from vocations.serializers import VocationSerializer
from items.serializers import ItemSerializer


class CharacterCreationSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    missions = MissionSerializer(read_only=True, many=True)
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = [
            "gold",
            "experience",
            "level",
            "health_points",
            "strength",
            "intellect",
            "agility",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class CharacterUpdateSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    vocation = VocationSerializer(read_only=True)
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = [
            "gold",
            "experience",
            "level",
            "health_points",
            "strength",
            "intellect",
            "agility",
        ]
        extra_kwargs = {"password": {"write_only": True}}
