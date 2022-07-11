from rest_framework import serializers

from .models import Artisan


class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = ["id", "name"]
        read_only_fields = ["id"]
