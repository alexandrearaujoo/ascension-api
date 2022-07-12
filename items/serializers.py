from rest_framework import serializers

from .models import Item
from artisans.serializers import ArtisanSerializer

from characters.serializer import CharacterSerializer


class ItemSerializer(serializers.ModelSerializer):
    owner = CharacterSerializer(read_only=True)
    artisan = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "type",
            "price",
            "level_required",
            "owner",
            "artisan",
        ]
        read_only_fields = ["id", "artisan"]

    def get_artisan(self, obj):
        return obj.artisan.name if obj.artisan else "Unidentified Artisan"
