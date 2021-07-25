from django.urls import path
from lottery_api import views

app_name = 'tickets'

urlpatterns = [
    path('', ticketsViewSet.as_view(), name='tickets')
]
