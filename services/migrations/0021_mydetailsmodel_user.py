# Generated by Django 4.1.7 on 2024-03-26 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0020_rename_address_deliverydetailsmodel_delivery_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydetailsmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
