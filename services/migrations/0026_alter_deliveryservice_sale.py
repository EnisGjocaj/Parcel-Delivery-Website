# Generated by Django 5.0.3 on 2024-04-03 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_deliveryservice_sale_alter_sale_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryservice',
            name='sale',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.sale'),
        ),
    ]