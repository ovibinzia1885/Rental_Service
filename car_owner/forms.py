from django import forms
from .models import *
from customer.models import *


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'car_name',
            'model_number',
            'vehicle_type',
            'price',
            'description',
            'image',
        ]


class ReservationStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['approval']
