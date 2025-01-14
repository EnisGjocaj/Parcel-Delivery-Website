# Generated by Django 4.1.7 on 2024-02-23 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0008_deliverydetailsmodel_returndetailsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveryGuaranteeOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_guarantee', models.BooleanField(default=False)),
                ('text_message', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='mydetailsmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='deliveryDetailsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.deliverydetailsmodel')),
                ('guarantee_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.deliveryguaranteeoptions')),
                ('return_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.returndetailsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
