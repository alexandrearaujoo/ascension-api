from rest_framework import serializers
from django.core.validators import MinValueValidator

from accounts.serializer import AccountInMissionsSerializer

from .models import Missions


class MissionSerializer(serializers.ModelSerializer):
    created_by = AccountInMissionsSerializer(read_only=True)

    class Meta:
        model = Missions
        fields = [
            "id",
            "description",
            "name",
            "experience",
            "level_required",
            "gold",
            "created_by",
        ]
        extra_kwargs = {
            "experience": {"validators": [MinValueValidator(0)]},
            "level_required": {"validators": [MinValueValidator(0)]},
            "gold": {"validators": [MinValueValidator(0)]},
            "xp": {"validators": [MinValueValidator(0)]},
        }


class GetMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = [
            "id",
            "description",
            "name",
            "experience",
            "level_required",
            "gold",
        ]
