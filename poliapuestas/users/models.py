from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Client(models.Model):
    """Model Client"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=20, blank=False, null=False, verbose_name='Identificación')
    virtual_wallet = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Puntos acumulados')
    age = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Edad')


    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'