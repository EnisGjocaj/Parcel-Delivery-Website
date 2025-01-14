# Generated by Django 5.0.3 on 2024-04-03 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_remove_deliveryservice_sale_percentage_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryservice',
            name='sale',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_service', to='services.sale'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sale_instance', to='services.deliveryservice'),
        ),
    ]
