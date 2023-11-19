import random
import string
from django.urls import reverse
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

VEHICLE_TYPES = (
    ('cabriolet', 'Cabriolet'),
    ('convertible', 'Convertible'),
    ('coupe', 'Coupe'),
    ('crossover', 'Crossover'),
    ('hatchback', 'Hatchback'),
    ('pickup', 'Pickup'),
    ('roadster', 'Roadster'),
    ('suv', 'SUV'),
    ('sedan', 'Sedan'),
    ('truck', 'Truck'),
    ('van', 'Van'),
    ('wagon', 'Wagon'),
    ('other', 'Other'),
)
FUEL_TYPES = (
    ('gas', 'Gas'),
    ('electric', 'Electric'),
    ('hybrid', 'Hybrid'),
    ('hydrogen', 'Hydrogen'),
    ('other', 'Other'),
)
# Create your models here.
class Automobile(models.Model):
    # id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2200), MinValueValidator(1875)])
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    vehicleType = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    gasOrElectric = models.CharField(max_length=11, choices=FUEL_TYPES)
    topSpeed = models.FloatField(default=2, null=True)
    zeroToSixty = models.FloatField(default=99, null=True)
    displacement = models.FloatField(default=0.1, null=True)
    range = models.FloatField(default=1, null=True) 

    def get_update_url(self):
        return reverse('automobile-update', kwargs={'id': self.id})
    
    def get_delete_url(self):
        return reverse('automobile-delete', kwargs={'id': self.id})

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'  

    def slug_generator(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=20))

    class Meta:
        verbose_name = 'Automobile'
        verbose_name_plural = 'Automobiles'


class ElectricCar(models.Model):
    # id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2200), MinValueValidator(1875)])
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    vehicleType = models.CharField(max_length=20)
    range = models.FloatField(default=1) 

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'
    
    class Meta:
        verbose_name = 'Electric Car'
        verbose_name_plural = 'Electric Cars'


class iceCar(models.Model):
    # id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2200), MinValueValidator(1875)])
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    vehicleType = models.CharField(max_length=20)
    displacement = models.FloatField(default=0.1)

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'
    
    class Meta:
        verbose_name = 'I.C.E. Car'
        verbose_name_plural = 'I.C.E. Cars'
