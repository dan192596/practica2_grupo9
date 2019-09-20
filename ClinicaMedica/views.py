from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile
# Create your views here.
def index(request):
    return HttpResponse("Esta es mi primera vista")

@login_required
def index(request):
    if request.user.is_authenticated:
        username = request.user.username

    else:
        username = 'No esta logeado'

    context = {'username': username}
    return  render(request, '', context)

@login_required
def profile(request):
    return render(request, '')

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('log:perfil')

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return  render(request, 'register.html', context)

def ListaClientes(request):
    ListaClientes = ClientProfile.objects.values('user', 'cui').distinct()
    return render(request, 'ListaClientes.html', {'ListaClientes':ListaClientes})