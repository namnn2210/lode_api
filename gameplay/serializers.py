from rest_framework import serializers
from .models import Order, UserProfile
from server.serializer import CitySerializer, SubGameSerializer


class OrderSerializer(serializers.ModelSerializer):
    city = CitySerializer()  # Include the CitySerializer for the 'city' field
    mode = SubGameSerializer()  # Include the SubgameSerializer for the 'mode' field

    class Meta:
        model = Order
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
