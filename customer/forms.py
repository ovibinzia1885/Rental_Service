from customer.models import *
from django import forms


class ReservationForm(forms.ModelForm):

    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Reservation
        fields = ['date', 'location_from', 'location_to', 'total_price']
