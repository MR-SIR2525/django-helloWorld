# Generated by Django 4.2.2 on 2023-08-28 23:00
"""We are transfering data from the ICE cars and Electric cars tables to the Automobiles table.
   The reason for this consolidation is that it seems weird to have three separate tables where
   there is some overlap in data across different tables.\n
   
   So the plan is to delete the ICE cars and Electric cars models after migrating the data. Then, 
   I will create a new model/table called 'personal computers' and put some data in there to  
   have some variety."""

from django.db import migrations, models

def copy_data(apps, schema_editor):
    # Get the models for the two tables
    elecCars = apps.get_model('helloWorld', 'electriccar')
    DestinationModel = apps.get_model('helloWorld', 'automobile')

    # Copy the data from the source table to the destination table
    for row in elecCars.objects.all():
        new_row = DestinationModel()
        new_row.year = row.year
        new_row.make = row.make
        new_row.model = row.model
        new_row.vehicleType = row.vehicleType
        new_row.gasOrElectric = 'electric' #added for Automobile
        new_row.topSpeed = 1 #added for Automobile (add real value later)
        new_row.zeroToSixty = 99 #added for Automobile (add real value later)
        new_row.displacement = None # set the value of the missing field to the corresponding value in the source table
        new_row.range = row.range
        new_row.save()
    
class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0007_icecar_data_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='displacement',
            field=models.FloatField(default=0.1, null=True)), 
        
        #absolutely vital this runs AFTER the above migration
        migrations.RunPython(copy_data),
    ]
