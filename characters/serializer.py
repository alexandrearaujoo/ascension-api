from django.shortcuts import get_object_or_404
from rest_framework import serializers
from characters.helpers import vocation_status_modifier
from vocations.models import Vocation

from .models import Character

from missions.serializers import GetMissionSerializer

from accounts.serializer import AccountSerializer

from vocations.serializers import VocationSerializer
from items.serializers import ItemSerializer


class CharacterCreationSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    missions = GetMissionSerializer(read_only=True, many=True)
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = [
            "id",
            "nickname",
            "level",
            "experience",
            "health_points",
            "gold",
            "strength",
            "intellect",
            "agility",
            "vocation",
            "items",
            "missions",
            "account",
        ]
        read_only_fields = [
            "gold",
            "experience",
            "level",
            "health_points",
            "strength",
            "intellect",
            "agility",
        ]

    def create(self, validated_data):
        vocation = get_object_or_404(Vocation, pk=validated_data["vocation"].id)
        validated_data = vocation_status_modifier(10, vocation, validated_data)
        return Character.objects.create(**validated_data)


class CharacterUpdateSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    vocation = VocationSerializer(read_only=True)
    missions = GetMissionSerializer(read_only=True, many=True)
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = [
            "id",
            "nickname",
            "level",
            "experience",
            "health_points",
            "gold",
            "strength",
            "intellect",
            "agility",
            "vocation",
            "items",
            "missions",
            "account",
        ]
        read_only_fields = [
            "gold",
            "experience",
            "level",
            "health_points",
            "strength",
            "intellect",
            "agility",
        ]
