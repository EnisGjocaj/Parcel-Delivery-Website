# Generated by Django 4.1.7 on 2024-02-27 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_alter_servicepacketingdeliverymainmodel_user_booking_data_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryservice',
            name='serviceModel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.servicemodel'),
        ),
    ]