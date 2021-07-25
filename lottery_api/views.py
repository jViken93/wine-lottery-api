from django.shortcuts import render
from rest_framework.views import APIView
from lottery_api import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from lottery_api import models

class LotteryRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LotteryRegistrationSerializers
    queryset = models.LotteryRegistration.objects.all()

class ticketsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TicketsSerializers
    queryset = models.Tickets.objects.all()
