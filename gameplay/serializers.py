from rest_framework import serializers
from .models import Order
from authentication.models import UserProfile
from server.serializer import CitySerializer, SubGameSerializer
from authentication.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    city = CitySerializer()  # Include the CitySerializer for the 'city' field
    mode = SubGameSerializer()  # Include the SubgameSerializer for the 'mode' field
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
