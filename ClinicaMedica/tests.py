from django.test import TestCase, Client
from .models import ClientProfile
from .forms import *
import json
from django.urls import reverse, resolve

class TestURLS(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url= reverse('CM:index')
        self.profile_url= reverse('CM:perfil')
        self.login_url = reverse('CM:login')
        self.logout_url = reverse('CM:logout')
        
        self.user = User.objects.create(
               username="gary",
               email="gary@gmail.com", 
               first_name="garyjoan",
               last_name="ortiz",
               password="garyortiz"
               )
        user = User.objects.create(email="garyjoan@gmail.com",username="garyjoan")
        self.create_user = ClientProfile(user=user,address="guatemala", phone=12345, cui=123454984983)
        self.create_user.save() 

    def test_index_page(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'index.html')

    def test_profile_page(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code,302)
        

    def test_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_page(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code,302)

    def test_UserProfileForm_valid(self):
        form = UserProfileForm(data={
              'address':"guatemala",
              'phone':122334})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserProfileForm_invalid(self):
        form = UserProfileForm(data={
            'addrss': "",
             'phone': "mp",
            })
        self.assertFalse(form.is_valid())

    def test_ExtendedUserCreationForm_valid(self):
        form = ExtendedUserCreationForm(data={
            'username':"garyJK",
            'email':"gary@gmail.com",
            'first_name':"gary", 
            'last_name':"ortiz",
            'password1':"garyjoan09", 
            'password2':"garyjoan09"
        })
        self.assertTrue(form.is_valid())
    def test_ExtendedUserCreationForm_invalid(self):
        form = ExtendedUserCreationForm(data={
            'username':"garyJK",
            'email':"gary@gmail.com",
            'first_name':"gary", 
            'last_name':"ortiz",
            'password1':"garyjoan09", 
            'password2':"garyjo"
        })
        self.assertFalse(form.is_valid())    

    def test_get_username(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_get_username_field(self):
        user = User.objects.get(id=1)
        expected_object_name = user.username
        self.assertEquals(expected_object_name, str(user))

    def test_ListaClientes_is_resolved(self):
        url = reverse('CM:ListaClientes')        
        self.assertEquals(resolve(url).url_name,'ListaClientes')

    def test_InfoCita_is_resolved(self):
        url = reverse('CM:InfoCita')
        self.assertEquals(resolve(url).url_name,'InfoCita')
    def test_CitaForm_valid(self):
        form = CitaForm(data={
            'cui': "2488258790101", 
            'description': "Esta es la descripcion", 
            'sintomas': "Estos son los sintomas", 
            'prescripcion': "Esta es la prescipcion", 
            'fecha': "2019-09-20", 
            'hora': "01:00"
        })
        self.assertTrue(form.is_valid())

    def test_ListaClientes_page(self):
        response = self.client.get(reverse('CM:ListaClientes'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'ListaClientes.html')
    
    def test_InfoCita_page(self):
        response = self.client.get(reverse('CM:InfoCita'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'Cita.html')