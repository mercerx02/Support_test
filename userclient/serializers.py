from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Ticket

class UserTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title','body']

class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tickets']

class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'body', 'owner']
