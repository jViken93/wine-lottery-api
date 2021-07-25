from django.shortcuts import render
from rest_framework.views import APIView
from lottery_api import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from lottery_api import models
from rest_framework.decorators import action
from django.db.models import Max
import random



class LotteryRegistrationViewSet(viewsets.ModelViewSet):
    """View class for Lottery Registration"""
    serializer_class = serializers.LotteryRegistrationSerializers
    queryset = models.LotteryRegistration.objects.all()

class ticketsViewSet(viewsets.ModelViewSet):
    """View class for tickets"""
    serializer_class = serializers.TicketsSerializers
    queryset = models.Tickets.objects.all()

    @action(detail=False, name='get_winner')
    def get_winner(self, request, pk=None):
        """Method for drawing a winner"""
        max_id = models.Tickets.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)
            winner = models.Tickets.objects.filter(pk=pk).first()
            count = models.Tickets.objects.count()
            if winner and winner.is_winner == False and count <= 5:
                winner.is_winner = True
                winner.save()
                return Response(f'Winner is {winner.participant}')
            else:
                return Response('All the winners have been drawn! Congratulations to all the winners')
