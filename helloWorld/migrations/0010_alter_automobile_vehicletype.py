# Generated by Django 4.2.2 on 2023-08-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0009_alter_automobile_range_alter_automobile_topspeed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='vehicleType',
            field=models.CharField(choices=[('cabriolet', 'Cabriolet'), ('convertible', 'Convertible'), ('coupe', 'Coupe'), ('crossover', 'Crossover'), ('hatchback', 'Hatchback'), ('pickup', 'Pickup'), ('roadster', 'Roadster'), ('suv', 'SUV'), ('sedan', 'Sedan'), ('truck', 'Truck'), ('van', 'Van'), ('wagon', 'Wagon'), ('other', 'Other')], max_length=20),
        ),
    ]
