from django.contrib import admin

from .models import Automobile, iceCar, ElectricCar

# Register your models here.
admin.site.register(Automobile)
admin.site.register(iceCar)
admin.site.register(ElectricCar)
