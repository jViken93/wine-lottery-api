# Generated by Django 3.2.5 on 2021-08-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery_api', '0004_alter_tickets_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lotteryregistration',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='lotteryregistration',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
