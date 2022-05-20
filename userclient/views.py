from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from django.contrib.auth.models import User
from api.models import Ticket
from api.permissions import isSupporter


class UserViewSet(ModelViewSet):
    """ViewSet for views associated with the User model """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [isSupporter]


class TicketViewSet(viewsets.GenericViewSet):
    """
   GenericViewSet to display all own tickets to the user who authenticated.
    And also to create a new ticket.

    """
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer

    def list(self, request)-> Response:

        tickets = Ticket.objects.filter(owner=request.user).values()
        return Response({"tickets": serializers.UserTicketsSerializer(tickets, many=True).data})

    def create(self, request)-> Response:

        new_ticket = Ticket.objects.create(
            title=request.data['title'],
            body=request.data['body'],
            owner=request.user,
        )

        return Response({'ticket': serializers.TicketSerializer(new_ticket).data})

    permission_classes = [permissions.IsAuthenticated]
