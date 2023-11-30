from django.test import TestCase
from django.urls import reverse

from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

class BetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', password='test_password')
        self.category = Category.objects.create(description='Test Category')


    # def test_create_bet(self):
    #     # Crea una instancia de Bet
    #     bet = Bet.objects.create(
    #         title='Test Bet',
    #         date_start='2023-01-01T00:00:00Z',
    #         date_end='2023-01-02T00:00:00Z',
    #         state='A',
    #         winner=self.user,
    #         result='Test Result',
    #         category=self.category,
    #         price_min=10,
    #         price_max=100
    #     )
    #     # Verifica que la instancia se haya creado correctamente
    #     self.assertEqual(bet.title, 'Test Bet')
    #     self.assertEqual(bet.state, 'A')
    #     self.assertEqual(bet.winner, self.user)
    #     self.assertEqual(bet.result, 'Test Result')
    #     self.assertEqual(bet.category, self.category)


    def test_raffle_view(self):
        # Autentica al usuario (simulación)
        self.client.login(username='testuser', password='testpassword')

        # URL para la vista
        url = reverse('raffle-list')

        # Datos del formulario
        data = {
            'title': 'Test Raffle',
            'date_start': '2023-01-01T00:00:00Z',
            'date_end': '2023-01-02T00:00:00Z',
            'state': 'A',
            'first_winner': self.user.id,
            'participants': [self.user.id],
            'category': self.category.id,
            'price': 50,
        }
        data2 = {
            'title': 'Test Raffle2',
            'date_start': '2023-01-01T00:00:00Z',
            'date_end': '2023-01-02T00:00:00Z',
            'state': 'B',
            'first_winner': self.user.id,
            'participants': [self.user.id],
            'category': self.category.id,
            'price': 100,
        }

        response = self.client.post(url, data=data)
        response = self.client.post(url, data=data2)

        # estado HTTP 200
        self.assertEqual(response.status_code, 201)

        #objeto Raffle en la base de datos
        self.assertEqual(Raffle.objects.count(), 2)
        raffle2 = Raffle.objects.get(id=2)

        self.assertEqual(raffle2.title, 'Test Raffle2')
        print(raffle2.id)
        url = reverse('raffle-detail', args=[raffle2.id])

        update_data = {
            'title': 'Test Raffle Update',
            'date_start': '2023-01-01T00:00:00Z',
            'date_end': '2023-01-02T00:00:00Z',
            'state': 'B',
            'first_winner': self.user.id,
            'participants': [self.user.id],
            'category': self.category.id,
            'price': 1500,
        }
        response = self.client.put(url, data=update_data)

        # Estado HTTP 200
        self.assertEqual(response.status_code, 200)

        # Actualiza Raffle de la base de datos
        raffle2.refresh_from_db()

        # Verifica actualizacion
        self.assertEqual(raffle2.title, 'Test Raffle Update')







