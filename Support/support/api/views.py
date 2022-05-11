from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from django.contrib.auth.models import User
from .models import Ticket,Message
from .permissions import isSupporter


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [isSupporter]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [isSupporter]

class CreateTicketVIEW(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AllTicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [isSupporter]

class UsersTicketAPIView(APIView):
    def get(self,request):
        tickets = Ticket.objects.filter(owner=request.user).values()
        return Response({"tickets":serializers.UserTicketsSerializer(tickets,many=True).data})

    permission_classes = [permissions.IsAuthenticated]


class MessagesList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



