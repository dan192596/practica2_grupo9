from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm,UserProfileForm
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

    context = {'form': form, 'profile_form': profile_form}
    return  render(request, 'register.html', context)

def ListaClientes(request):
    ListaClientes = ClientProfile.objects.values('user', 'cui').distinct()
    return render(request, 'ListaClientes.html', {'ListaClientes':ListaClientes})

def InfoCliente(request, codigo):
    ListaClientes = ClientProfile.objects.filter(cui=codigo).distinct()
    return render(request, 'Cliente.html', {'ListaClientes':ListaClientes})