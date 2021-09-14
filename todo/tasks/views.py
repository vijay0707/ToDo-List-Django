from django.shortcuts import render, redirect
from .models import Taskmodel
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def home(request):

    tasks = Taskmodel.objects.all()
    
    context = {
        'tasks':tasks,
    }
    return render(request, 'tasks/taskview.html', context)

@login_required(login_url='login')
def create_task(request):

    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {
        'form':form,
    }

    return render(request, 'tasks/createTask.html', context)

@login_required(login_url='login')
def delete_task(request, id):
    task = Taskmodel.objects.get(id=id)
    if request.method == 'POST':
            task.delete()
            return redirect('home')
    
    context = {
        'task':task,
    }    

    return render(request, 'tasks/deleteTask.html', context)


@login_required(login_url='login')
def update_task(request, id):
    
    task = Taskmodel.objects.get(id=id)

    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {
        'task':'task',
        'form':form,
    }

    return render(request, 'tasks/updateTask.html', context)

# USER

def registerUser(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, 'Account was Created for'+' '+ username)
            return redirect('login')

    context ={
        'form':form
    }

    return render(request, 'tasks/register.html', context)

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("success")
            return redirect('home')

        else:
            messages.warning(request, 'Username or Password is incorrect')
            
    context ={}

    return render(request, 'tasks/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User logged out successfully')
    return redirect('login')
    

