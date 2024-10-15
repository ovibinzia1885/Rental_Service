from django.urls import path
from .views import *


urlpatterns = [
    path('customer_booking_reservation/<int:id>/', customer_booking_reservation, name='customer_booking_reservation'),
    path('booking_seat_amount/<int:vehicle>/<int:location_from>/<int:location_to>/', booking_seat_amount,
         name='booking_seat_amount'),
    path('customer_own_reservation_list/', customer_own_reservation_list, name='customer_own_reservation_list'),
]
