from rest_framework import serializers
from .models import corona19_model


class Corona19Serializer(serializers.ModelSerializer):
    class Meta:
        model = corona19_model
        fields = "__all__"