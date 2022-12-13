from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from patient.models import Patient
from django.contrib.auth.models import User
from django.db.models import *
from .models import *

# Create your views here.
def home(request):
   return render(request,'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password =password)
        if user is not None:
            patient_user = Patient.objects.get(user=user)
            if patient_user is not None:
               messages.info(request,patient_user)
               login(request, user)
               return redirect('/Patient/Dashboard')
        else:
            messages.info(request , "Invaild username or password")
    return render(request , 'login.html')

def register(request):
    
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
          form = CreateNewUser()
    return render(request , 'signup.html' , {'form': form})
def sinout(request):
    logout(request)
    return redirect('login')