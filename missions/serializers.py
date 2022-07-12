from rest_framework import serializers
from django.core.validators import MinValueValidator

from accounts.serializer import PatronInMissionsSerializer

from .models import Missions


class MissionSerializer(serializers.ModelSerializer):
    created_by = PatronInMissionsSerializer(read_only=True)

    class Meta:
        model = Missions
        fields = [
            'id', 
            'description', 
            'name', 
            'experience', 
            'level_required', 
            'gold', 
            'xp', 
            'created_by'
        ]
        extra_kwargs = {
            "experience": {"validators": [MinValueValidator(0)]},
            "level_required": {"validators": [MinValueValidator(0)]},
            "gold": {"validators": [MinValueValidator(0)]},
            "xp": {"validators": [MinValueValidator(0)]},
        }
