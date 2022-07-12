from rest_framework import serializers

from .models import Patron


class PatronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
<<<<<<< HEAD
        fields = ["id", "username", "password", "classification"]
=======
        fields = ["id", 'username','password','classification']
>>>>>>> 9039b30fa121ca45d2db5ce482a887773949f426
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Patron.objects.create_superuser(**validated_data)


class PatronLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
