# Generated by Django 4.1.7 on 2024-02-27 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_servicepacketingdeliverymainmodel_servicemodelinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryservice',
            name='serviceModel',
        ),
    ]
