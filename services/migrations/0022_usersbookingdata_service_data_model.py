# Generated by Django 4.1.7 on 2024-03-27 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_mydetailsmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersbookingdata',
            name='service_data_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.serviceusermodel'),
        ),
    ]