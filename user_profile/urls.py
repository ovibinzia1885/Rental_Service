from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('sign-up/', registration, name='sign_up'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('password_change/', password_change, name='password_change'),

    path('vehicle_details/<int:id>/', vehicle_details, name='vehicle_details'),
    path('vehicle/', vehicle, name='vehicle'),

    path('vehicle_type_vehicle/<int:id>/', vehicle_type_vehicle, name='vehicle_type_vehicle'),

    path('subscribe/', subscribe, name='subscribe'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),

]
