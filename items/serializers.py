from rest_framework import serializers

from .models import Item
from artisans.serializers import ArtisanSerializer

from characters.serializer import CharacterSerializer


class ItemSerializer(serializers.ModelSerializer):
    owner = CharacterSerializer(read_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "type",
            "price",
            "level_required",
            "owner",
            "artisan"
        ]
        read_only_fields = ["id", "artisan"]
