from rest_framework import generics
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description']


class CreateTicket(generics.CreateAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class RetrieveTicket(generics.RetrieveAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

