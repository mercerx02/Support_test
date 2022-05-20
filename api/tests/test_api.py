from rest_framework.test import APITestCase
from rest_framework import status




class MessageAPITestCase(APITestCase):
    def test_get(self):
        url = "http://127.0.0.1:8000/api/tickets/message/"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class TicketListAPITestCase(APITestCase):
    def test_get(self):
        url = "http://127.0.0.1:8000/api/support/tickets/"
        response = self.client.get(url)
        self.assertEqual(response.data,status.HTTP_200_OK)
