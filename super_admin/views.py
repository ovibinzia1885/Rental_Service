from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *
from car_owner.filters import *
from car_owner.models import *
from customer.models import *
from .filters import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def customer(request):
    user = User.objects.all()
    customer = user.filter(user_type='customer')
    MyFilter = CustomerFilter(request.GET, queryset=customer)
    customer = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(customer, 5)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    context = {
        'customer': customer,
        'MyFilter': MyFilter
    }
    return render(request, 'super_admin/customer.html', context)


def car_owner(request):
    user = User.objects.all()
    car_owner = user.filter(user_type='car_owner')
    MyFilter = CustomerFilter(request.GET, queryset=car_owner)
    car_owner = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(car_owner, 5)
    try:
        car_owner = paginator.page(page)
    except PageNotAnInteger:
        car_owner = paginator.page(1)
    except EmptyPage:
        car_owner = paginator.page(paginator.num_pages)
    context = {
        'car_owner': car_owner,
        'MyFilter': MyFilter
    }
    return render(request, 'super_admin/car_owner.html', context)


def create_vehicle_type(request):
    form = VehicleTypeForm()
    if request.method == "POST":
        form = VehicleTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_vehicle_type')
    context = {
        'form': form
    }
    return render(request, 'super_admin/vehicle_type/create.html', context)


def list_vehicle_type(request):
    vehicle_type = VehicleType.objects.all()
    MyFilter = VehicleTypeFilter(request.GET, queryset=vehicle_type)
    vehicle_type = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(vehicle_type, 5)
    try:
        vehicle_type = paginator.page(page)
    except PageNotAnInteger:
        vehicle_type = paginator.page(1)
    except EmptyPage:
        vehicle_type = paginator.page(paginator.num_pages)
    context = {
        'vehicle_type': vehicle_type,
        'MyFilter': MyFilter
    }
    return render(request, 'super_admin/vehicle_type/list.html', context)


def update_vehicle_type(request, id):
    vehicle_type = VehicleType.objects.get(id=id)
    form = VehicleTypeForm(instance=vehicle_type)
    if request.method == 'POST':
        form = VehicleTypeForm(request.POST, instance=vehicle_type)
        if form.is_valid():
            form.save()
            return redirect('list_vehicle_type')
    context = {
        'form': form
    }
    return render(request, 'super_admin/vehicle_type/update.html', context)


def delete_vehicle_type(request, id):
    vehicle_type = VehicleType.objects.get(id=id)
    if request.method == 'POST':
        vehicle_type.delete()
        return redirect('list_vehicle_type')
    context = {
        'vehicle_type': vehicle_type
    }
    return render(request, 'super_admin/vehicle_type/delete.html', context)


def create_location_from(request):
    form = LocationFrom()
    if request.method == "POST":
        form = LocationFrom(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            location_form = form.cleaned_data['from_name']
            to = To()
            to.to_name = location_form
            to.save()
            print(location_form)
            f.save()
            return redirect('list_location_from_to')
    context = {
        'form': form
    }
    return render(request, 'super_admin/from/create.html', context)


def list_location_from_to(request):
    f = From.objects.all()
    t = To.objects.all()
    MyFilter = LocationFromFilter(request.GET, queryset=f)
    MyFilter1 = LocationToFilter(request.GET, queryset=t)
    f = MyFilter.qs
    t = MyFilter1.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(f, 5)
    paginator1 = Paginator(t, 5)
    try:
        f = paginator.page(page)
        t = paginator1.page(page)
    except PageNotAnInteger:
        f = paginator.page(1)
        t = paginator1.page(1)
    except EmptyPage:
        f = paginator.page(paginator.num_pages)
        t = paginator1.page(paginator.num_pages)
    context = {
        'f': f,
        't': t,
        'MyFilter': MyFilter,
        'MyFilter1': MyFilter1,
    }
    return render(request, 'super_admin/from/list.html', context)


def update_location_from_to(request, id):
    f = From.objects.get(id=id)
    t = To.objects.get(id=id)
    form = LocationFrom(instance=f)
    if request.method == 'POST':
        form = LocationFrom(request.POST, instance=f)
        if form.is_valid():
            f = form.save(commit=False)
            print(f)
            location_to = form.cleaned_data['from_name']
            print(location_to)
            t.to_name = location_to
            t.save()
            f.save()
            return redirect('list_location_from_to')
    context = {
        'form': form
    }
    return render(request, 'super_admin/from/update.html', context)


def delete_location_from_to(request, id):
    f = From.objects.get(id=id)
    t = To.objects.get(id=id)
    if request.method == 'POST':
        f.delete()
        t.delete()
        return redirect('list_location_from_to')
    context = {
        'f': f
    }
    return render(request, 'super_admin/from/delete.html', context)


def create_distance(request):
    form = DistanceForm()
    if request.method == "POST":
        form = DistanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_distance')
    context = {
        'form': form
    }
    return render(request, 'super_admin/distance/create.html', context)


def list_distance(request):
    distance = Distance.objects.all()
    MyFilter = DistanceFilter(request.GET, queryset=distance)
    distance = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(distance, 5)
    try:
        distance = paginator.page(page)
    except PageNotAnInteger:
        distance = paginator.page(1)
    except EmptyPage:
        distance = paginator.page(paginator.num_pages)
    context = {
        'distance': distance,
        'MyFilter': MyFilter
    }
    return render(request, 'super_admin/distance/list.html', context)


def update_distance(request, id):
    distance = Distance.objects.get(id=id)
    form = DistanceForm(instance=distance)
    if request.method == 'POST':
        form = DistanceForm(request.POST, instance=distance)
        if form.is_valid():
            form.save()
            return redirect('list_distance')
    context = {
        'form': form
    }
    return render(request, 'super_admin/distance/update.html', context)


def delete_distance(request, id):
    distance = Distance.objects.get(id=id)
    if request.method == 'POST':
        distance.delete()
        return redirect('list_distance')
    context = {
        'distance': distance
    }
    return render(request, 'super_admin/distance/delete.html', context)


def super_admin_vehicle_list(request):
    vehicle = Vehicle.objects.all()
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
    return render(request, 'super_admin/vehicle_list.html', context)


def car_owner_own_vehicle(request, id):
    user = User.objects.get(id=id)
    vehicle = Vehicle.objects.filter(car_owner=user)
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
    return render(request, 'super_admin/car_owner_own_vehicle_list.html', context)


def super_admin_change_vehicle_status(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = VehicleStatusUpdateForm(instance=vehicle)
    if request.method == "POST":
        form = VehicleStatusUpdateForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('super_admin_vehicle_list')
    context = {
        'form': form
    }
    return render(request, 'super_admin/approval_status_form.html', context)


def super_admin_reservation_list(request, id):
    vehicle = Vehicle.objects.get(id=id)
    reservation = Reservation.objects.filter(vehicle_name=vehicle)
    context = {
        'reservation': reservation
    }
    return render(request, 'super_admin/reservation_list.html', context)


def subscribe_list(request):
    subscribe = Subscribe.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(subscribe, 5)
    try:
        subscribe = paginator.page(page)
    except PageNotAnInteger:
        subscribe = paginator.page(1)
    except EmptyPage:
        subscribe = paginator.page(paginator.num_pages)
    context = {
        'subscribe': subscribe
    }
    return render(request, 'super_admin/subscribe.html', context)


def contact_list(request):
    contact = Contact.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(contact, 5)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    context = {
        'contact': contact
    }
    return render(request, 'super_admin/contact.html', context)
