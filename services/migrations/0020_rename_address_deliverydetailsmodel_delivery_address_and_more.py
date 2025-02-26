# Generated by Django 4.1.7 on 2024-03-26 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_remove_deliveryservice_servicemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverydetailsmodel',
            old_name='address',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='deliverydetailsmodel',
            old_name='full_name',
            new_name='delivery_full_name',
        ),
        migrations.RenameField(
            model_name='deliverydetailsmodel',
            old_name='postal_code',
            new_name='delivery_postal_code',
        ),
        migrations.RenameField(
            model_name='returndetailsmodel',
            old_name='address',
            new_name='return_address',
        ),
        migrations.RenameField(
            model_name='returndetailsmodel',
            old_name='full_name',
            new_name='return_full_name',
        ),
        migrations.RenameField(
            model_name='returndetailsmodel',
            old_name='postal_code',
            new_name='return_postal_code',
        ),
    ]
