from rest_framework import serializers
from .models import Vocation


class VocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocation
        fields = "__all__"
