from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm

class CreationUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class Creationspecification(ModelForm):
    class Meta:
        model = Specialization
        widgets = {
            'name': TextInput(attrs={
            'placeholder': 'enter a specification',
            'required' : True,
              })
            }
        fields = ['name']
        
class CreationDoctor(ModelForm):
    class Meta:
        model = Doctor
        widgets = {
            'specialization': TextInput(attrs={
            'placeholder': 'select specification',
            'required' : True,
              }),
            'name': TextInput(attrs={
                'placeholder': 'enter Doctor Name',
                'required' : True,
              }),
            'email': EmailInput(attrs={
                'placeholder': 'enter Doctor Email',
                'required' : True,
              }),
            
            'phone_number': TextInput(attrs={
                'placeholder': 'enter salary ',
                'required' : True,
              }),
            'address': TextInput(attrs={
                'placeholder': 'enter address ',
              }),
        }
        
        fields = ['user','Specialization','name','email','phone_number','gender','salary','address','profile_img']
        
        

