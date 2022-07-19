from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Vocation


class VocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocation
        fields = "__all__"
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Vocation.objects.all(),
                        message="This vocation already exists.",
                    )
                ]
            }
        }
