from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
User = get_user_model()  # getting user model
# class Doctor

class Doctor(models.Model):
    GenderChoices = (
        ('male', 'male'),
        ('female', 'female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_images', default='default-profile-image-png-1-Transparent-Images.png')
    phone_number = models.CharField(max_length=20, blank=True, null=True, default="None")
    address = models.CharField(max_length=100, blank=True, null=True, default="None")
    salary = models.IntegerField(default=250)
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GenderChoices, blank=True, null=True, default="male")
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs)


def create_Doctor(sender, **kwargs):
    if kwargs['created']:
        print(type(kwargs['instance']))
        Doctor.objects.create(user=kwargs['instance'])

post_save.connect(create_Doctor, sender=User)
