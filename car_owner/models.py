from django.db import models
from user_profile.models import User
from super_admin.models import *


class Vehicle(models.Model):
    APPROVAL = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    car_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.CharField(verbose_name='Vehicle Name', max_length=200)
    model_number = models.CharField(verbose_name='Model Number', max_length=200)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, verbose_name='Vehicle Type')
    price = models.FloatField(verbose_name='Price In KM')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    image = models.ImageField(upload_to='vehicle_image', verbose_name='Vehicle Image')
    approval = models.CharField(max_length=15, choices=APPROVAL, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.car_name)
