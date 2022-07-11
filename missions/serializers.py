from rest_framework import serializers
from django.core.validators import MinValueValidator

from patrons.serializer import PatronSerializer

from .models import Missions


class MissionSerializer(serializers.ModelSerializer):
    created_by = PatronSerializer(read_only=True)

    class Meta:
        model = Missions
        fields = "__all__"
        extra_kwargs = {
            "experience": {"validators": [MinValueValidator(0)]},
            "level_required": {"validators": [MinValueValidator(0)]},
            "gold": {"validators": [MinValueValidator(0)]},
            "xp": {"validators": [MinValueValidator(0)]},
        }
