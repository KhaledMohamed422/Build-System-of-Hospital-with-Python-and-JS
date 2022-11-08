from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password =password)
        if user is not None:
            login(request ,user)
            return HttpResponse("Done loged in ")
    return render(request , 'login.html')


def register(request):
    form = CreateNewUser(request.POST)
    masage = []
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            print("ok")
            return redirect('login')
    else:
          form = CreateNewUser()
    return render(request , 'signup.html' , {'form': form})



