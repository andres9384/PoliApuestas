# DRF
from rest_framework import viewsets
# Models
from .models import *
# Serializers
from .serializers import *


class BetModelViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RaffleModelViewSet(viewsets.ModelViewSet):
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer
