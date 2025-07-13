from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo

# Dashboard view
@login_required(login_url='login')
def dashboard(request):
    task = Todo.objects.filter(user= request.user)
    return render(request , 'dashboard.html',{'task':task})

# Add Task View
@login_required(login_url='login')
def add(request):
    if request.method == "POST":
         form  = TodoRegistration(request.POST)
         if form.is_valid():
             todo = form.save(commit=False)
             todo.user = request.user
             todo.save()
             messages.success(request , "Task Added")
             return redirect('dashboard')
    else:
        form = TodoRegistration()
    return render(request , 'add.html' , {'form':form})

#Edit task View
@login_required(login_url='login')
def edit(request ,task_id ):
    task = get_object_or_404(Todo, id = task_id, user = request.user)
    if request.method == 'POST':
        form = TodoRegistration(request.POST , instance=task)
        if form.is_valid():
            form.save()
            messages.success(request , "Task Updated")
            return redirect('dashboard')
    else:
        form = TodoRegistration(instance=task)
    
    return render(request , 'edit.html' , {'form':form})
