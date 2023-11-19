from django import forms
from crispy_forms.layout import Field

from .models import Automobile, ElectricCar, iceCar


class addAutomobileForm(forms.ModelForm):
    """Used to create and update Automobile in views."""
    topSpeed = forms.FloatField(required=False)
    zeroToSixty = forms.FloatField(required=False)
    displacement = forms.FloatField(required=False)
    range = forms.FloatField(required=False)

    class Meta:
        model = Automobile
        fields = '__all__'


class AutomobileIdForm(forms.Form):
    """Designed to be used/placed alongside the addAutomobileForm. This exists because
       we need to be able to append or add automobile_id to the POST data from 
       the update form."""
    automobile_id = forms.IntegerField(
        required=True,
        label='ID # of Automobile'
    )
class confirmUpdateAutomobile(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="I chose the right Automobile id # to update."
    )


class deleteAutomobileForm(forms.Form):
    automobile_id = forms.IntegerField(
        required = True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Automobile id #',
        })
    )
    confirm = forms.BooleanField(
        required=True,
        label="I understand what deleting means and have double checked the id given."
    )




class addElectricCarForm(forms.ModelForm):
    class Meta:
        model = ElectricCar
        fields = '__all__'

class addIceCarForm(forms.ModelForm):
    class Meta:
        model = iceCar
        fields = '__all__'


class CustomCheckbox(Field):
    template = 'custom_checkbox.html'