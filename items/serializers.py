from rest_framework import serializers

from .models import Item
from artisans.serializers import ArtisanSerializer
# from characters.serializers import CharacterSerializer



class Item(serializers.ModelSerializer):
    # character = CharacterSerializer(read_only=True)
    artisan = ArtisanSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'price', 'level_required', 'artisan', 'character']
        read_only_fields = ['id', 'artisan', 'character']        
