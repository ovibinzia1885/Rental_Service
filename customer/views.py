from django.shortcuts import render, redirect
from customer.models import *
from .forms import *
from django.http import JsonResponse


def customer_booking_reservation(request, id):
    vehicle = Vehicle.objects.get(id=id)
    print('vehicle = ', vehicle)
    form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        print(form)
        if form.is_valid():
            b = form.save(commit=False)
            b.vehicle_name = vehicle
            b.customer_name = request.user
            b.total_price = request.POST['total_price']
            b.save()
            vehicle.save()
            return redirect('home')
    context = {
        'vehicle': vehicle,
        'form': form
    }
    return render(request, 'create_booking.html', context)


def booking_seat_amount(request, vehicle, location_from, location_to):
    total_amount = 0
    vehicle = Vehicle.objects.get(id=vehicle)
    print('vehicle = ', vehicle)
    location_from = From.objects.get(id=location_from)
    print('location from = ', location_from)
    location_to = To.objects.get(id=location_to)
    print('location To = ', location_from)
    distance_found = Distance.objects.get(location_from=location_from, location_to=location_to)
    print('distance_found = ', distance_found)
    distance = distance_found.distance
    print('distance = ', distance)
    print('vehicle per km price  = ', vehicle.price)
    total_amount = (vehicle.price * int(distance))
    print('total_amount = ', total_amount)
    return JsonResponse({'amount': total_amount}, safe=False)


def customer_own_reservation_list(request):
    reservation = Reservation.objects.filter(customer_name=request.user)
    context = {
        'reservation': reservation
    }
    return render(request, 'customer_own_reservation_list.html', context)
