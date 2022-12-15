from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
User = get_user_model()  # getting user model
# class Patient


class Patient(models.Model):
    
    GenderChoices = (
    ('male','male'),
    ('female', 'female'),
)
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    # use default profile image in intial in profile
    profile_img = models.ImageField( upload_to='profile_images',  default='default-profile-image-png-1-Transparent-Images.png')
    descrption = models.TextField(max_length=500, blank=True, null=True,default="None")
    phone_number = models.CharField(max_length=20, blank=True, null=True ,default="None")
    address = models.CharField(max_length=100, blank=True, null=True,default="None")
    city = models.CharField(max_length=100, blank=True, null=True,default="None")
    gender = models.CharField(max_length=6,choices=GenderChoices,blank=True, null=True,default="male")
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)


def create_Patient(sender, **kwargs):
    if kwargs['created']:
        new_Patient = kwargs['instance']
        Patient.objects.create(user=new_Patient,name=new_Patient.first_name,email=new_Patient.email)

post_save.connect(create_Patient, sender=User)
