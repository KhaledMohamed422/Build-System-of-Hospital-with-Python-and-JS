from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Specialization(models.Model):
    Specialization_name = (
        ('Diagnostic_radiology', 'Diagnostic_radiology'),
        ('Anesthesiology', 'Anesthesiology'),
        ('Dermatology', 'Dermatology'),
        ('Blood', 'Blood'),
    )
    name = models.CharField(
        max_length=100, choices=Specialization_name, blank=True, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    GenderChoices = (
        ('male', 'male'),
        ('female', 'female'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    Specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(
        upload_to='profile_images', default='default-profile-image-png-1-Transparent-Images.png')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(
        max_length=100, blank=True, null=True, default="None")
    salary = models.IntegerField(default=250)
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GenderChoices, blank=True, null=True, default="male")

    def __str__(self):
        return self.user.username


class docter_schedule(models.Model):

    Date_Book = models.DateField(blank=True, null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, blank=True, null=True)
    data_8to10 = models.BooleanField(default=False)
    data_10to12 = models.BooleanField(default=False)
    data_12to1 = models.BooleanField(default=False)
    data_1to2 = models.BooleanField(default=False)
    data_2to4 = models.BooleanField(default=False)
    data_4to6 = models.BooleanField(default=False)

    def __str__(self):
        x = ""
        if self.data_8to10 != False:
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("1012")
        if self.data_10to12 != False:
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("1201")
        if self.data_12to1 != False:
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("0102")
        if self.data_1to2 != False:
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("0204")
        if self.data_2to4 != False:
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("0406")
        if self.data_4to6 != False:
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("Full")
        if x == "":
            x = str(self.doctor.user)+'/'+str(self.Date_Book)+'/'+str("0810")
        return x

    # def save(self, *args, **kwargs):
    #     super(Doctor, self).save(*args, **kwargs)


# def create_Doctor(sender, **kwargs):
#     if kwargs['created']:
#         print(type(kwargs['instance']))
#         Doctor.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_Doctor, sender=User)
