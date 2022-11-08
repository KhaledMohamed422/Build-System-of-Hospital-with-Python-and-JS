from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewUser
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_user(request):
    return render(request , 'login.html')

def register(request):
    return render(request , 'signup.html')