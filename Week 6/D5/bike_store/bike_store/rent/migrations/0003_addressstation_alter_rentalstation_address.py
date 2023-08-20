# Generated by Django 4.2.4 on 2023-08-19 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_vehicleatrentalstation_rental_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='rentalstation',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.addressstation'),
        ),
    ]