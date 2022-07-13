from rest_framework import serializers
from django.core.validators import MinValueValidator

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    artisan = serializers.SerializerMethodField()
    power = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "type",
            "power",
            "price",
            "level_required",
            "owner",
            "artisan",
        ]
        read_only_fields = ["id", "owner", "artisan"]
        extra_kwargs = {
            "price": {"validators": [MinValueValidator(0)]},
            "level_required": {"validators": [MinValueValidator(0)]},
        }

    def get_artisan(self, obj):
        return obj.artisan.name if obj.artisan else "Unidentified Artisan."

    def get_owner(self, obj):
        return obj.owner.name if obj.owner else "This item don't have an owner."

    def get_power(self, obj):
        power_value = round((obj.level_required + 1) * 1.3)
        characteristics = "Attack"

        if obj.type == "SH" or obj.type == "AR" or obj.type == "LE":
            characteristics = "Defense"
            return f"{characteristics} power of {power_value}pts."

        return f"{characteristics} power of {power_value}pts."
