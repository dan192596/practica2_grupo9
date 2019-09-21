from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm, CitaForm
from .models import Cita, ClientProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

    