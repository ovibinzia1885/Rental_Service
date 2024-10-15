from django.shortcuts import render, redirect, reverse
from user_profile.models import *
from user_profile.forms import *
from car_owner.models import *
from super_admin.models import *
from car_owner.filters import *
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
User = get_user_model()


def home(request):
    vehicle = Vehicle.objects.filter(approval='Approved')[0:6]
    vehicle_type = VehicleType.objects.all()
    context = {
        'vehicle': vehicle,
        'vehicle_type': vehicle_type,
    }
    return render(request, 'index.html', context)


def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(id=id)
    context = {
        'vehicle': vehicle
    }
    return render(request, 'vehicle_details.html', context=context)


def vehicle(request):
    vehicle = Vehicle.objects.filter(approval='Approved')
    MyFilter = VehicleFilter(request.GET, queryset=vehicle)
    vehicle = MyFilter.qs
    context = {
        'vehicle': vehicle,
        'MyFilter': MyFilter,
    }
    return render(request, 'vehicle.html', context)


def vehicle_type_vehicle(request, id):
    vehicle_type = VehicleType.objects.get(id=id)
    vehicle = Vehicle.objects.filter(vehicle_type=vehicle_type)
    print('vehicle = ', vehicle)
    context = {
        'vehicle': vehicle,
        'vehicle_type': vehicle_type,

    }
    return render(request, 'vehicle_type_vehicle.html', context=context)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        user_authentication = authenticate(request, username=user, password=password)
        print(user_authentication)
        if user_authentication is not None:
            auth_login(request, user_authentication)
            if user_authentication.is_superuser:
                return redirect(reverse('home'))
            elif user_authentication.user_type == 'customer':
                return redirect(reverse('home'))
            elif user_authentication.user_type == 'car_owner':
                return redirect(reverse('home'))
        else:
            message = "Your email And Password Is Wrong"
            context = {
                'message': message,
            }
            return render(request, 'login.html', context=context)
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context=context)


def profile(request):
    return render(request, 'profile/profile.html')


def update_profile(request):
    form = UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form
    }
    return render(request, 'profile/update_profile.html', context=context)


def password_change(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('login'))
        else:
            pass
    else:
        form = PasswordForm(request.user)
        context = {
            'form': form
        }
        return render(request, 'profile/password_change.html', context=context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscribe = Subscribe()
        subscribe.email = email
        subscribe.save()
        return redirect('home')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        con = Contact()
        con.name = name
        con.email = email
        con.subject = subject
        con.message = message
        con.save()
        return redirect('home')
    else:
        return render(request, 'contact.html')
