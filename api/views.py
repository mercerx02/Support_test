from rest_framework import generics, permissions,mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import serializers
from .models import Ticket,Message
from .permissions import isSupporter


class AllTicketList(generics.ListAPIView):

    """Support view - shows all existing tickets"""
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [isSupporter]


class MessagesList(generics.ListCreateAPIView):

    """View for messages between User and Support"""

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    permission_classes = [permissions.IsAuthenticated]

