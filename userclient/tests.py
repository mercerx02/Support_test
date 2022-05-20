
from rest_framework import status
from rest_framework.test import APITestCase


class TicketAPITestCase(APITestCase):
    def test_get(self):
        url = 'http://127.0.0.1:8000/api/users/tickets/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class UsersAPITestCase(APITestCase):
    def test_get(self):
        url = "http://127.0.0.1:8000/api/users/support/"
        response = self.client.get(url)
        self.assertEqual(response.data,status.HTTP_200_OK)


