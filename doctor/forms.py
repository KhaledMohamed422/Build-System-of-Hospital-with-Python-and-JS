from .models import *
from django.forms import ModelForm

class ProfileDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','email','gender','phone_number','address','profile_img']