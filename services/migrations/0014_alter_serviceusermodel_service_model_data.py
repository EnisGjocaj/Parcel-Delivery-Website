# Generated by Django 4.1.7 on 2024-02-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_remove_servicemodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceusermodel',
            name='service_model_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.deliveryservice'),
        ),
    ]
