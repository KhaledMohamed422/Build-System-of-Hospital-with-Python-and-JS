from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Create your views here.
from .models import *
from doctor.models import *
import datetime


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
def bookAppointment_1(request):
    patient_user = Patient.objects.get(user=request.user)
    specialization_doctor = Specialization.objects.all()
    
    if request.method == "POST":
        Date = request.POST.get('Date')
        speciality = request.POST.get('speciality') 
        check = datetime.datetime.strptime(Date +" 08:15:27.243860", '%Y-%m-%d %H:%M:%S.%f').date() < datetime.datetime.now().date()
        
        if check :
            context = {
                'patient':patient_user,
                'specialization_doctor' : specialization_doctor,
                'check' :check
            }
            return render(request, 'dashbord-form1book.html',context)    
        else:
            return redirect('/Patient/BookAppointment_2')
    context = {
                'patient':patient_user,
                'specialization_doctor' : specialization_doctor,
            }
    return render(request, 'dashbord-form1book.html',context)


@login_required(login_url='login')  
def bookAppointment_2(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'dashbord-form2book.html',{'patient':patient_user})

  
@login_required(login_url='login')  
def appointHistory(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'dashbord-AppointHistory.html',{'patient':patient_user})


