from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Dashboard(request):
   return render(request,'manager/dashbord.html')

def AddDoctor(request):
   return render(request,'manager/add-doctor.html')

def myAppointment(request):
   return render(request,'manager/appointment.html')

def ManagePatient(request):
   return render(request,'manager/patient.html')

def ManageUser(request):
   return render(request,'manager/user.html')

def ManageDoctor(request):
   return render(request,'manager/manage_doctor.html')

def EditSpecification(request):
   return render(request,'manager/edit-specification.html')

def PatientData(request):
   return render(request,'manager/view_data_patient.html')