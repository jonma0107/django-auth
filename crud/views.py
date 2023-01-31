from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import Task


def home(request):
  return render(request, 'home.html')

def tasks(request):
  lista = Task.objects.filter(user=request.user)
  return render(request, 'tasks.html', {'objetos': lista})

def create_task(request):
  if request.method == 'GET':
    return render(request, 'create_task.html', {
    'form': TaskForm
    })
  else:
    if request.POST['description'] == '':
      create = render(request, 'create_task.html', {
        'form': TaskForm,
        'error': 'la descripcion debe llenarse'
        })
      return create
      
    else:
      form = TaskForm(request.POST)
      task_new = form.save(commit=False)
      task_new.user = request.user
      task_new.save()
      return redirect('tasks')  

def signup(request):
  if request.method == 'GET':
    return render(request, 'signup.html', {
      "form": UserCreationForm
    })
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('tasks')
      except:
        return render(request, 'signup.html', {
          "form": UserCreationForm,
          "error": 'usuario ya existe'
          })
    return render(request, 'signup.html', {
      "form": UserCreationForm,
      "error": 'contraseñas erradas'
      })

def cerrar(request):
  logout(request)
  return redirect("home")

def abrir(request):
  if request.method == 'GET':
    return render(request, 'abrir.html', {
    'form': AuthenticationForm
    })
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'abrir.html', {'form': AuthenticationForm, 'error': 'Credenciales no validas'})
    else:
      login(request, user)
      return redirect('tasks')







