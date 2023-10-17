# DRF
from rest_framework import serializers
# Models
from .models import *


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RaffleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raffle
        fields = '__all__'
