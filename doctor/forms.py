from .models import *
from django.forms import ModelForm

class ProfileDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','email','gender','phone_number','address','profile_img']
class Appointmentform(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name','patient','doctor','phone_number','data_time','descrption']
class Specializationform(ModelForm):
    class Meta:
        model = Specialization
        fields = ['name']