from django.urls import path
from .views import *

urlpatterns = [
    path('create_vehicle_type/', create_vehicle_type, name='create_vehicle_type'),
    path('list_vehicle_type/', list_vehicle_type, name='list_vehicle_type'),
    path('update_vehicle_type/<int:id>/', update_vehicle_type, name='update_vehicle_type'),
    path('delete_vehicle_type/<int:id>/', delete_vehicle_type, name='delete_vehicle_type'),

    path('create_location_from/', create_location_from, name='create_location_from'),
    path('list_location_from_to/', list_location_from_to, name='list_location_from_to'),
    path('update_location_from_to/<int:id>/', update_location_from_to, name='update_location_from_to'),
    path('delete_location_from_to/<int:id>/', delete_location_from_to, name='delete_location_from_to'),

    path('customer/', customer, name='customer'),
    path('car_owner/', car_owner, name='car_owner'),
    path('super_admin_vehicle_list/', super_admin_vehicle_list, name='super_admin_vehicle_list'),
    path('car_owner_own_vehicle/<int:id>/', car_owner_own_vehicle, name='car_owner_own_vehicle'),
    path('super_admin_change_vehicle_status/<int:id>/', super_admin_change_vehicle_status,
         name='super_admin_change_vehicle_status'),

    path('create_distance/', create_distance, name='create_distance'),
    path('list_distance/', list_distance, name='list_distance'),
    path('update_distance/<int:id>/', update_distance, name='update_distance'),
    path('delete_distance/<int:id>/', delete_distance, name='delete_distance'),

    path('super_admin_reservation_list/<int:id>/', super_admin_reservation_list, name='super_admin_reservation_list'),
    path('subscribe_list/', subscribe_list, name='subscribe_list'),
    path('contact_list/', contact_list, name='contact_list'),

]
