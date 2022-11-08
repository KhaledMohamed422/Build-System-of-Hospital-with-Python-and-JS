from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password =password)
        if user is not None:
            login(request ,user)
            return HttpResponse("Done loged in ")
        else:
            messages.info(request , "Invaild username or password")
    return render(request , 'login.html')

def register(request):
    form = CreateNewUser(request.POST)
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
          form = CreateNewUser()
    return render(request , 'signup.html' , {'form': form})