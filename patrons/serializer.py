from rest_framework import serializers

from .models import Patron


class PatronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = ["id", "username", "password", "classification"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Patron.objects.create_superuser(**validated_data)


class PatronLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
