from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Create your views here.
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required 

@login_required(login_url='login')  
def dashboard(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'patient_dashbord.html',{'patient':patient_user})

@login_required(login_url='login')  
def profile(request):
    object_Patient = Patient.objects.get(user=request.user)
    
    if request.method == "POST":
        form = ProfilePatient(request.POST , request.FILES ,  instance = object_Patient)
        if form.is_valid:
            form.save()  
            return redirect('/Patient/Dashboard')
    else:
        form = ProfilePatient(instance = object_Patient)
    return render(request, 'dashbord-profile.html',{'form':form,'patient':object_Patient})

@login_required(login_url='login')  
def bookAppointment(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'dashbord-app.html',{'patient':patient_user})

@login_required(login_url='login')  
def appointHistory(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'dashbord-my-app.html',{'patient':patient_user})
