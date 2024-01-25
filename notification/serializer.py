from rest_framework import serializers
from .models import NotificationModel, NotificationCategoryModel
from authentication.serializers import UserSerializer


class NotificationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCategoryModel
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    category = NotificationCategorySerializer()
    user = UserSerializer()

    class Meta:
        model = NotificationModel
        fields = '__all__'
