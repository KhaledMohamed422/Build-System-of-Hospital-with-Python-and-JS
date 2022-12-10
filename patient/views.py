from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages  # Create your views here.


def dashboard(request):
    return render(request, 'dashbord.html')


def profile(request):
    return render(request, 'dashbord-profile.html')


def bookAppointment(request):
    return render(request, 'dashbord-app.html')


def appointHistory(request):
    return render(request, 'dashbord-my-app.html')
