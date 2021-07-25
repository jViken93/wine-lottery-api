from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string

class LotteryRegistration(models.Model):
    """Lottery user registration"""
    full_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    tickets_to_buy = models.IntegerField()

    def get_tickets(self):
        return self.tickets_to_buy

    def __str__(self):
        """Return the model last and first name as String"""
        return self.full_name

class Tickets(models.Model):
    """Model for tickets"""
    participant = models.ForeignKey('LotteryRegistration', on_delete = models.CASCADE)
    ticket = models.CharField(max_length=100, blank=True, unique=True)
    is_winner = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        """Override the save method to add a custom code to ticket field"""
        letters = string.ascii_lowercase
        self.ticket = ''.join(random.choice(letters)for i in range(8))
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the ticket as String"""
        return self.ticket

@receiver(post_save, sender=LotteryRegistration)
def signal_receiver(sender, instance, created, **kwargs):
    """When a participant is registerd, the amount of tickets they buy
        will automatically be added to the tickets model"""
    if created:
       for i in range(instance.tickets_to_buy):
           Tickets.objects.create(participant=instance)
