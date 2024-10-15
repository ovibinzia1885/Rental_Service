from django import forms
from .models import *
from car_owner.models import *


class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name']


class LocationFrom(forms.ModelForm):
    class Meta:
        model = From
        fields = ['from_name']


class DistanceForm(forms.ModelForm):
    class Meta:
        model = Distance
        fields = ['location_from', 'location_to', 'distance']


class VehicleStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['approval']
