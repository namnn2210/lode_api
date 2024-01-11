from rest_framework import serializers
from .models import Game, Subgame, City, Rate


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class SubGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgame
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
