# Generated by Django 4.2.4 on 2023-08-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_vehicleatrentalstation_rental_station_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicleatrentalstation',
            name='rental_station',
        ),
        migrations.AddField(
            model_name='rentalstation',
            name='vehicle',
            field=models.ManyToManyField(to='rent.vehicle'),
        ),
    ]
