# Generated by Django 5.0.3 on 2024-04-16 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_alter_deliveryservice_sale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryservice',
            name='sale',
        ),
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage_value', models.IntegerField()),
                ('selected_service_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.deliveryservice')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]