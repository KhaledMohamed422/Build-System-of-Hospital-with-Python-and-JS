from .models import *
from django.forms import ModelForm

class ProfileDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','gender','email','profile_img','phone_number','address']


