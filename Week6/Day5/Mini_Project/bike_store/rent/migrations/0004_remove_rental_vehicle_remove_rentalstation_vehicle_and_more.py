# Generated by Django 4.2.4 on 2023-08-18 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_remove_vehicleatrentalstation_rental_station_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='rentalstation',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='rental',
            name='vehicle_at_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.vehicleatrentalstation'),
        ),
        migrations.AddField(
            model_name='vehicleatrentalstation',
            name='rental_station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rent.rentalstation'),
        ),
    ]