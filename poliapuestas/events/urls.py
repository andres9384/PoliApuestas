# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter
# Views
from .views import *

router = DefaultRouter()

router.register('bet', BetModelViewSet, basename='bet')
router.register('raffle', RaffleModelViewSet, basename='raffle')
router.register('category', CategoryModelViewSet, basename='category')


urlpatterns = [
    path('api/', include(router.urls)),
]