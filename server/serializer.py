from rest_framework import serializers
from .models import Game, Subgame, City, Rate, Banking, BalanceTransaction

from banks.serializer import BankSerializer

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


class BankingSerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = Banking
        fields = '__all__'


class BalanceTransactionSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = BalanceTransaction
        fields = '__all__'
