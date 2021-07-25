from django.contrib import admin
from lottery_api import models
# Register your models here.

admin.site.register(models.LotteryRegistration)
admin.site.register(models.Tickets)
