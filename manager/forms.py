from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, EmailInput , PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreationUser(UserCreationForm):
    class Meta:
        model = User
        widgets = {
            'username': TextInput(attrs={
            'placeholder': 'enter user name',
            'required' : True,
              }),
            }
        fields = ['username','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(CreationUser, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password from numbers and letters of the Latin alphabet'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Password confirmation'})

        

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
              
            'name': TextInput(attrs={
                'placeholder': 'enter Doctor Name',
                'required' : True,
                'id' : 'name',
                
              }),
            
            'email': EmailInput(attrs={
                'placeholder': 'enter Doctor Email',
                'required' : True,
              }),
            
            'phone_number': TextInput(attrs={
                'placeholder': 'enter a number ',
                'required' : True,
              }),
            
            'address': TextInput(attrs={
                'placeholder': 'enter address ',
              }),
        }
        
        fields = ['user','Specialization','name','email','phone_number','gender','salary','address','profile_img']
        
        

