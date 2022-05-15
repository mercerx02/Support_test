from rest_framework.test import APITestCase
from rest_framework import status


class TicketAPITestCase(APITestCase):

    def test_get(self):
        url = 'http://127.0.0.1:8000/api/tickets/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


