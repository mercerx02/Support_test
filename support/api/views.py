from rest_framework import generics, permissions,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import viewsets
from rest_framework.decorators import action

from . import serializers
from django.contrib.auth.models import User
from .models import Ticket,Message
from .permissions import isSupporter

class UserViewSet(ModelViewSet):
    """ViewSet для представлений, связанных с моделью User """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [isSupporter]

class TicketViewSet(viewsets.GenericViewSet):
    """GenericViewSet для отоброжения всех собственных тикетов пользователю, который произвел аутенфикацию.
    А так же для создания нового тикета.
    
    """
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer

    def list(self,request):
        tickets = Ticket.objects.filter(owner=request.user).values()
        return Response({"tickets": serializers.UserTicketsSerializer(tickets, many=True).data})


    def create(self,request):
        new_ticket = Ticket.objects.create(
            title = request.data['title'],
            body = request.data['body'],
            owner = request.user,
        )
        return Response({'ticket':serializers.TicketSerializer(new_ticket).data})



    permission_classes = [permissions.IsAuthenticated]




class AllTicketList(generics.ListAPIView):
    """Представление для суппорта - показывает все существующие тикеты"""
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [isSupporter]


class MessagesList(generics.ListCreateAPIView):

    """Представление для сообщений между Юзером и Суппортом"""

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    permission_classes = [permissions.IsAuthenticated]

