# Generated by Django 4.1.7 on 2024-02-25 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_alter_servicemodel_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicemodel',
            name='price',
        ),
    ]
