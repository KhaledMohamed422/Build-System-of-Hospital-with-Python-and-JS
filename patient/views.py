from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Create your views here.
from .models import *
from doctor.models import *
import datetime
from .forms import *
from django.contrib.auth.decorators import login_required 
Date = None
speciality = None
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
    list_available_dates = [] # return bookAppointment_1

    if request.method == "POST":
        Date = request.POST.get('Date')
        speciality = request.POST.get('speciality')
        check = datetime.datetime.strptime(Date + " 08:15:27.243860",
                                           '%Y-%m-%d %H:%M:%S.%f').date() < datetime.datetime.now().date()
        id = Specialization.objects.get(name=speciality)
        list_of_doctor = Doctor.objects.all().filter(Specialization=id)
        for doctor in list_of_doctor:
            free_time = docter_schedule.objects.filter(Date_Book=Date,doctor=doctor).first()

            if free_time == None:
               free_time = docter_schedule.objects.create(Date_Book=Date,doctor=doctor)
               free_time.save()
            if free_time.data_8to10 == False:
                list_available_dates.append(free_time)


            elif  free_time.data_10to12 == False:
                list_available_dates.append(free_time)


            elif free_time.data_12to1 == False:
                list_available_dates.append(free_time)

            elif free_time.data_1to2 == False:
                list_available_dates.append(free_time)

            elif free_time.data_2to4 == False:
                list_available_dates.append(free_time)

            elif free_time.data_4to6 == False:
                list_available_dates.append(free_time)
        
        
        if check :
            context = {
                'patient':patient_user,
                'specialization_doctor' : specialization_doctor,
                'check' :check
            }
            return render(request, 'dashbord-form1book.html',context)    
        else:
            return redirect('BookAppointment_2' , slug = str(str(Date)+"_"+str(speciality)))
    context = {
                'patient':patient_user,
                'specialization_doctor' : specialization_doctor,
            }
    return render(request, 'dashbord-form1book.html',context)


@login_required(login_url='login')  
def bookAppointment_2(request,slug):
    slug = str(slug)
    Date= str(slug[0 : slug.index('_')])
    speciality = str(slug[slug.index('_') + 1: ])
    

    patient_user = Patient.objects.get(user=request.user)

    return render(request, 'dashbord-form2book.html',{'patient':patient_user})

  
@login_required(login_url='login')  
def appointHistory(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'dashbord-AppointHistory.html',{'patient':patient_user})


