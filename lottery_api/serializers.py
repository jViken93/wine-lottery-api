from rest_framework import serializers
from lottery_api import models

class LotteryRegistrationSerializers(serializers.ModelSerializer):
    """serializers Lottery Registration items"""

    class Meta:
        model = models.LotteryRegistration
        fields = ('id', 'first_name', 'last_name', 'email', 'tickets_to_buy')

class TicketsSerializers(serializers.ModelSerializer):
    """serializers for ticket items"""

    """Set the method get_participants to participant field"""
    participant = serializers.SerializerMethodField('get_participant')

    class Meta:
        model = models.Tickets
        fields = ('id', 'participant', 'ticket', 'is_winner')

    def get_participant(self, obj):
        """Get the name of the participant instead of a number on forign key"""
        return(obj.participant.first_name)
