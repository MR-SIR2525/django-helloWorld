# Generated by Django 4.0.4 on 2022-09-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr', models.IntegerField(max_length=4)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=50)),
                ('vehicleType', models.CharField(max_length=20)),
                ('gasOrElectric', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='ElectricCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr', models.IntegerField(max_length=4)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=50)),
                ('vehicleType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='iceCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr', models.IntegerField(max_length=4)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=50)),
                ('vehicleType', models.CharField(max_length=20)),
            ],
        ),
    ]
