from django.urls import path
from .views import *

urlpatterns = [
    path('vehicle_list/', vehicle_list, name='vehicle_list'),
    path('vehicle_create/', vehicle_create, name='vehicle_create'),
    path('vehicle_update/<int:id>/', vehicle_update, name='vehicle_update'),
    path('vehicle_delete/<int:id>/', vehicle_delete, name='vehicle_delete'),

    path('reservation_list/<int:id>/', reservation_list, name='reservation_list'),
    path('car_owner_change_reservation_status/<int:id>/', car_owner_change_reservation_status,
         name='car_owner_change_reservation_status'),
]
