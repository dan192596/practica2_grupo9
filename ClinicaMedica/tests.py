from django.test import TestCase, Client
from .models import ClientProfile, TypeUser
from .forms import *
import json
from django.urls import reverse, resolve

# Create your tests here.
def test_ListaClientes_is_resolved(self):
    url = reverse('CM:ListaClientes')
    self.assertEquals(resolve(url).url_name,'ListaClientes')


class TestURLS(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url= reverse('CM:index')
        self.profile_url= reverse('CM:perfil')
        self.login_url = reverse('CM:login')
        self.logout_url = reverse('CM:logout')
        self.admin_url = reverse('CM:home_admin')
        self.new_user_url = reverse('CM:create_user')
        self.update_user_url = reverse('CM:update_user')
        self.delete_user_url = reverse('CM:delete_user')
        self.user = User.objects.create(
               username="gary",
               email="gary@gmail.com", 
               first_name="garyjoan",
               last_name="ortiz",
               password="garyortiz"
               )
        user = User.objects.create(email="garyjoan@gmail.com",username="garyjoan")
        self.create_user = ClientProfile(user=user,address="guatemala", phone=12345, cui=123454984983, type=4)
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

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_get_username_field(self):
        user = User.objects.get(id=1)
        expected_object_name = user.username
        self.assertEquals(expected_object_name, str(user))

    def test_get_home_admin_page(self):
        response = self.client.get(self.admin_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'homeAdmin.html')

    def test_get_create_user_admin_page(self):
        response = self.client.get(self.new_user_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'nuevo_usuario.html')

    def test_get_update_user_admin_page(self):
        response = self.client.get(self.update_user_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'update_usuario.html')

    def test_get_delete_user_admin_page(self):
        response = self.client.get(self.delete_user_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'delete_user.html')
        
    def test_TypeUser_create(self):
        self.type_user = TypeUser(nameType="test")
        self.type_user.save()

    def test_delete_user(self):
        response = self.client.post(self.delete_user_url,{
            'delete_value':1,
        })
        self.assertEquals(response.status_code,200)


def test_InfoCliente_is_resolved(self):
    url = reverse('CM:InfoCliente')
    self.assertEquals(resolve(url).url_name,'InfoCliente')

