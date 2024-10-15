import django_filters
from .models import *


class VehicleFilter(django_filters.FilterSet):
    car_name = django_filters.CharFilter(lookup_expr='icontains', label='Car Name ')
    model_number = django_filters.CharFilter(lookup_expr='icontains', label='Model Name')

    class Meta:
        model = Vehicle
        fields = ['car_name', 'model_number', 'vehicle_type', 'approval']
