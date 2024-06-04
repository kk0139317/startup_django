from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     pass

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    username = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    comments = models.BooleanField(default=False)
    candidates = models.BooleanField(default=False)
    offers = models.BooleanField(default=False)
    push_notifications = models.CharField(max_length=20, choices=[('everything', 'Everything'), ('same_as_email', 'Same as email'), ('nothing', 'No push notifications')])

    def __str__(self):
        return self.username
