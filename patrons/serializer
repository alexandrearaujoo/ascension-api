from rest_framework import serializers

from .models import Patron


class PatronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class PatronLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
