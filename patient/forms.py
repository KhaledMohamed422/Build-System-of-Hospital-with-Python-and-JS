from .models import *
from django.forms import ModelForm

class ProfilePatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name','email','gender','phone_number','address','city','profile_img']
        
        
  