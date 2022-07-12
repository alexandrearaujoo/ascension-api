from rest_framework import serializers

from .models import Artisan

class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = ["id", "name", "items"]
        read_only_fields = ["id"]
        depth = 1
