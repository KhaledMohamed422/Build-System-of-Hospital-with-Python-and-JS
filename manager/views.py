from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import * 
from doctor.models import *
from patient.models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Dashboard(request):
   return render(request,'manager/dashbord.html')

@login_required(login_url='login')
def AddDoctor(request):
   form = CreationDoctor()
   if request.method == 'POST':
      form = CreationDoctor(request.POST)
      if form.is_valid():
            form.save()
            return redirect('/Manager/Dashboard')  
   context = {
      'form' : form,
      'errors' : form.errors,
   }    
   return render(request,'manager/add-doctor.html',context)

@login_required(login_url='login')
def AddUser(request):
   form = CreationUser()
   if request.method == 'POST':
      form = CreationUser(request.POST)
      if form.is_valid():
            form.save()
            return redirect('/Manager/Dashboard')  
   context = {
      'form' : form,
      'errors' : form.errors,
   }    
   return render(request,'manager/add-user.html',context)    
    
@login_required(login_url='login')
def AddSpecification(request):
   form = Creationspecification()
   if request.method == 'POST':
      form = Creationspecification(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/Manager/Dashboard')  
   context = {
   'form' : form,
   'errors' : form.errors,
   }    
   return render(request,'manager/add-specification.html',context)
    
@login_required(login_url='login')
def myAppointment(request):
   Appointment_list = Appointment.objects.all()
   return render(request,'manager/appointment.html',{'Appointment_list' : Appointment_list})

@login_required(login_url='login')
def ManagePatient(request):
   Patient_list = Patient.objects.all()     
   return render(request,'manager/patient.html',{'Patient_list' : Patient_list})

@login_required(login_url='login')
def ManageUser(request):
   return render(request,'manager/user.html')

@login_required(login_url='login')
def ManageDoctor(request):
   return render(request,'manager/manage_doctor.html')

@login_required(login_url='login')
def PatientData(request):
   return render(request,'manager/view_data_patient.html')


@login_required(login_url='login')
def ManageSpecification(request):
   return render(request,'manager/view_data_patient.html')

@login_required(login_url='login')
def descrption(request,id):
    # descrption = request.POST['descrption'] 
    #  created_descrption = Appointment.objects.get(id = id)
    # created_descrption.descrption = descrption
    # created_descrption.save() 
    return render(request,'manager/descrption-form-.html',{'descrption_Paragrah' : Appointment.objects.get(id = id).descrption})
    # return redirect('/Patient/AppointHistory')       
