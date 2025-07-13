from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Home View
def home(request):
    return render(request, "home.html")


# Register View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request , user) 
            messages.success(request, "Registration complete, Now you can customize your Todo list")
            return redirect('add')
    else:
        form = RegistrationForm()
    return render(request , 'register.html', {"form":form})


# Login View
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request , user)
            messages.success(request, "Login successfull")
            return redirect('dashboard')
        else:
            messages.error(request , "Invalid Username or Password")
    return render(request , 'login.html')



# Logout View
@login_required(login_url = 'login')
def logout(request):
    auth_logout(request)
    messages.success(request , 'Logout Successfull')
    return redirect('login')
