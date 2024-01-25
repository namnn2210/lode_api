from rest_framework import serializers
from .models import SystemModel


class SystemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemModel
        fields = '__all__'
