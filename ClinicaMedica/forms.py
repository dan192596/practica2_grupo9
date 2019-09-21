from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile, Cita
from django import forms
from django.forms import ModelForm, DateInput, TimeInput

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name', 'last_name', 'password1', 'password2'}

    def save(self, commit=True):
        user =super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
        
class UserProfileForm(ModelForm):
    class Meta:
        model = ClientProfile
        fields = {'address', 'phone'}

class CitaForm(ModelForm):
    class Meta:
        model = Cita
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'hora': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)    

        self.fields['fecha'].input_formats = ('%Y-%m-%d',)
        self.fields['hora'].input_formats = ('%H:%M',)
        self.fields['cui'].label = "Ingrese CUI: "
        self.fields['description'].label = "Ingrese la descripcion de la cita: "
        self.fields['sintomas'].label = "Ingrese los sintomas del paciente: "
        self.fields['prescripcion'].label = "Ingrese la prescipcion realizada: "