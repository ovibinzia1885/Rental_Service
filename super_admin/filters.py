from django.contrib.auth.models import User
from .models import *
import django_filters
from user_profile.models import *


class CustomerFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains', label='UserName')
    phone_number = django_filters.CharFilter(lookup_expr='icontains', label='Phone Number')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', ]


class VehicleTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Vehicle Type')

    class Meta:
        model = VehicleType
        fields = ['name']


class LocationFromFilter(django_filters.FilterSet):
    from_name = django_filters.CharFilter(lookup_expr='icontains', label='From')

    class Meta:
        model = From
        fields = ['from_name']


class LocationToFilter(django_filters.FilterSet):
    to_name = django_filters.CharFilter(lookup_expr='icontains', label='To')

    class Meta:
        model = To
        fields = ['to_name']


class DistanceFilter(django_filters.FilterSet):
    class Meta:
        model = Distance
        fields = ['location_from', 'location_to']
