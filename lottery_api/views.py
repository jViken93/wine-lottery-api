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

        """Count how many have won"""
        all_winners = models.Tickets.objects.filter(is_winner = True)
        winners_count = all_winners.count()

        while winners_count <= 4:
            """get a random id number"""
            pk = random.randint(1, max_id)
            winner = models.Tickets.objects.filter(pk=pk, is_winner = False).first()

            if winner and winner.is_winner == False:
                winner.is_winner = True
                winner.save()
                winner_is = f'Vinneren er {winner.participant}'
                return Response({'Winner': winner_is})
        return Response({'Winner': 'Alle vinnere er trukket! Gratulerer til alle som vant'})

    @action(detail=False, name='get_all_winners')
    def get_all_winners(self, request, pk=None):
        """Returns all the the winners"""
        all_winners = models.Tickets.objects.filter(is_winner = True)
        serializer = serializers.TicketsSerializers(all_winners, many=True)
        return Response(serializer.data)
