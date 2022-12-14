from .models import *
from django.forms import ModelForm

class ProfilePatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name','gender','email','profile_img','descrption','phone_number','address','city']