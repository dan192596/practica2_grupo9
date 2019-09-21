from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForm,UserProfileForm
from .models import TypeUser, ClientProfile

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
    return render(request,"nuevo_usuario.html",context)

def updateUser(request):
    list = User.objects.all()
    context = {'list':list}
    return render(request,"update_usuario.html",context)

def deleteUser(request):
    if request.POST:
        id = request.POST['delete_value']
        User.objects.filter(id=id).delete()
    
    list = User.objects.all()
    context = {'list':list}
    return render(request,"delete_user.html",context)