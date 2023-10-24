# DRF
from rest_framework import viewsets
# Models
from .models import *
# Serializers
from .serializers import *




class BetModelViewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite ver, crear, actualizar o eliminar apuestas.

        :param models.Bet ViewSet.ModelViewSet
        :returns serializer_class BetSerializer
    """
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite ver, crear, actualizar o eliminar una categoria.
        :param models.Category ViewSet.ModelViewSet
        :returns serializer_class CategorySerializer
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RaffleModelViewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite ver, crear, actualizar o eliminar Rifas .
        :param models.Raffle ViewSet.ModelViewSet
        :returns serializer_class RaffleSerializer
    """
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer
