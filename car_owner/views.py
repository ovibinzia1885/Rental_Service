from django.shortcuts import render, redirect
from .forms import *
from .models import *
from customer.models import *
from .filters import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def vehicle_list(request):
    vehicle = Vehicle.objects.filter(car_owner=request.user)
    MyFilter = VehicleFilter(request.GET, queryset=vehicle)
    vehicle = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(vehicle, 5)
    try:
        vehicle = paginator.page(page)
    except PageNotAnInteger:
        vehicle = paginator.page(1)
    except EmptyPage:
        vehicle = paginator.page(paginator.num_pages)
    context = {
        'vehicle': vehicle,
        'MyFilter': MyFilter
    }
    return render(request, 'car_owner/vehicle/list.html', context)


def vehicle_create(request):
    form = VehicleForm()
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            v = form.save(commit=False)
            v.car_owner = request.user
            v.save()
            return redirect('vehicle_list')
    context = {
        'form': form
    }
    return render(request, 'car_owner/vehicle/create.html', context=context)


def vehicle_update(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = VehicleForm(instance=vehicle)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    context = {
        'form': form
    }
    return render(request, 'car_owner/vehicle/update.html', context)


def vehicle_delete(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    context = {
        'vehicle': vehicle
    }
    return render(request, 'car_owner/vehicle/delete.html', context)


def reservation_list(request, id):
    vehicle = Vehicle.objects.get(id=id)
    reservation = Reservation.objects.filter(vehicle_name=vehicle)
    context = {
        'reservation': reservation
    }
    return render(request, 'car_owner/vehicle/reservation_list.html', context)


def car_owner_change_reservation_status(request, id):
    reservation = Reservation.objects.get(id=id)
    form = ReservationStatusUpdateForm(instance=reservation)
    if request.method == "POST":
        form = ReservationStatusUpdateForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    context = {
        'form': form
    }
    return render(request, 'car_owner/reservation_approval_status_form.html', context)
