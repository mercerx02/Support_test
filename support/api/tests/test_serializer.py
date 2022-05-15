from api.serializers import TicketSerializer
from api.models import Ticket
from django.test import TestCase

class TicketSerializerTestCase(TestCase):
    def test_data(self):
        ticket_1 = Ticket.objects.create(title="TicketTest1",body="problem1")
        data = [TicketSerializer(ticket_1).data]

        expected_data = [

            {
                'id':ticket_1.id,
                'title': "TicketTest1",
                'body': "problem1"
            }
        ]

        self.assertEqual(data,expected_data)