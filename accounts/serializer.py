from rest_framework import serializers

from .models import Account

class AccountInMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", 'username','password','classification']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Account.objects.create_superuser(**validated_data)


class AccountLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
