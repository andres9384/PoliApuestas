from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    """Model Category"""
    description = models.CharField(max_length=50, blank=False, null=False, verbose_name='Descripción')

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.description


class Bet(models.Model):
    """Model bet"""
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Nombre Apuestas')
    date_start = models.DateTimeField(verbose_name='Fecha Inicio')
    date_end = models.DateTimeField(verbose_name='Fecha Fin')
    state = models.CharField(max_length=1, blank=False, null=False, verbose_name='Estado')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ganador')
    result = models.CharField(max_length=150, blank=False, null=False, verbose_name='Resultado')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    participants = models.ManyToManyField(User, blank=True, verbose_name='Participantes')
    price_min = models.PositiveBigIntegerField(blank=False, null=False, verbose_name='Precio Minimo')
    price_max = models.PositiveBigIntegerField(blank=False, null=False, verbose_name='Precio Maximo')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Apuesta"
        verbose_name_plural = 'Apuestas'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Raffle(models.Model):
    """Model raffle"""
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Nombre Apuestas')
    date_start = models.DateTimeField(verbose_name='Fecha Inicio')
    date_end = models.DateTimeField(verbose_name='Fecha Fin')
    state = models.CharField(max_length=1, blank=False, null=False, verbose_name='Estado')
    first_winner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Primer Ganador')
    participants = models.ManyToManyField(User, blank=True, verbose_name='Participantes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    price = models.PositiveBigIntegerField(blank=False, null=False, verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Rifa"
        verbose_name_plural = 'Rifas'
        ordering = ['-created']

    def __str__(self):
        return self.title

