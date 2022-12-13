from django.shortcuts import render

# Create your views here.
def Dashboard(request):
    return render(request, 'dr_dashbord.html')


def profile(request):
    return render(request, 'myprofile.html')


def myAppointment(request):
    return render(request, 'myappointment.html')

def patientslist(request):
    return render(request, 'patient.html')