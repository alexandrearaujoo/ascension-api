from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Artisan

from items.serializers import ItemSerializer


class ArtisanSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Artisan
        fields = ["id", "name", "items"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Artisan.objects.all(),
                        message="This artisan already exists.",
                    )
                ]
            }
        }
