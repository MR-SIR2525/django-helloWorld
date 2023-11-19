from django.urls import path, include

from .views import *

# app_name = 'carstats'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home', Home.as_view(), name='home'),
    path('carstats', carstats.as_view(), name='carstats'),

    path('automobile-stats', AutomobileList.as_view(), name='automobile-stats'),
    path('ice-car-stats', iceCarList.as_view(), name='ice-car-stats'),
    path('electric-car-stats', ElectricCarList.as_view(), name='electric-car-stats'),
    path('automobile/add', AutomobileCreate.as_view(), name='automobile-add'),
    path('automobile/delete', AutomobileDelete.as_view(), name='automobile-delete'),
    path('automobile/update', AutomobileUpdate.as_view(), name='automobile-update'),
    # path('automobile/<id>/update', executeAutomobileUpdate(), name='execute-automobile-update' ),
]
