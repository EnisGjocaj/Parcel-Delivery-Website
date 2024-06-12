# Generated by Django 4.1.7 on 2024-02-13 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0003_deliveryservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryservice',
            name='speed_unit',
            field=models.CharField(blank=True, choices=[('hours', 'Hours'), ('days', 'Days')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='deliveryservice',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliveryservice',
            name='speed',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]