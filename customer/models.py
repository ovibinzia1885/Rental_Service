from django.db import models
from super_admin.models import *
from car_owner.models import *


class Reservation(models.Model):
    APPROVAL = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Reservation Date')
    location_from = models.ForeignKey(From, on_delete=models.CASCADE, verbose_name='From ')
    location_to = models.ForeignKey(To, on_delete=models.CASCADE, verbose_name='To ')
    total_price = models.CharField(max_length=10, verbose_name='Total Price ')
    approval = models.CharField(max_length=15, choices=APPROVAL, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_name)
