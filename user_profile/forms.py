from django import forms
from user_profile.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(UserCreationForm):
    user_type_choice = (
        ('car_owner', 'car owner'),
        ('customer', 'customer'),
    )
    user_type = forms.ChoiceField(choices=user_type_choice, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['user_type', 'username', 'email', 'phone_number', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        user = User.objects.filter(phone_number__iexact=phone_number).exists()
        if user:
            raise ValidationError(_('You can not use this Phone Number.'))

        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))
        return email


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for username in self.fields.keys():
            self.fields[username].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'address', 'image']