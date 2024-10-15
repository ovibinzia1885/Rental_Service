from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings


class User(AbstractUser):
    user_type_choice = (
        ('car_owner', 'car owner'),
        ('customer', 'customer'),
    )
    user_type = models.CharField(max_length=10, choices=user_type_choice, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='profile_pics')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return str(self.email)


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
