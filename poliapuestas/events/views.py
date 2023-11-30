# DRF
from rest_framework import viewsets
# Models
from .models import *
# Serializers
from .serializers import *


class BetModelViewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite ver, crear, actualizar o eliminar apuestas.
        :param request.data
        :return BetSerializer
    """
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite ver, crear, actualizar o eliminar una categoria.
        :param request.data
        :return CategorySerializer
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RaffleModelViewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite ver, crear, actualizar o eliminar Rifas .
        :param request.data
        :return RaffleSerializer
    """
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer



