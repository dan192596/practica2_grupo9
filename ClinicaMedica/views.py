from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm, CitaForm
from .models import Cita, ClientProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TypeUser
# Create your views here.
def indexL(request):
    return render(request, 'index.html', {})

@login_required
def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'No esta logeado'
    context = {'username': username}
    return  render(request, 'perfil.html', context)

def ListaClientes(request):
    ListaClientes = ClientProfile.objects.values('user', 'cui').distinct()
    return render(request, 'ListaClientes.html', {'ListaClientes':ListaClientes})

def InfoCliente(request, codigo):
    ListaClientes = ClientProfile.objects.filter(cui=codigo).distinct()
    return render(request, 'Cliente.html', {'ListaClientes':ListaClientes})


#ADMINISTRADOR
def homeAdmin(request):
    return render(request,"homeAdmin.html",{})

def createUser(request):
    if request.POST:
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

        return render(request,"index.html")
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request,"newUserAdmin.html",context)

def updateUser(request):
    list = User.objects.all()
    context = {'list':list}
    return render(request,"updateUserAdmin.html",context)

def deleteUser(request):
    if request.POST:
        id = request.POST['delete_value']
        User.objects.filter(id=id).delete()
    
    list = User.objects.all()
    context = {'list':list}
    return render(request,"deleteUserAdmin.html",context)

def InfoCita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            print(form.data)            
            form.save()
            return HttpResponseRedirect(reverse('CM:index'))
    else: 
        form = CitaForm() 
        return render(request, "Cita.html", {'form': form})

    