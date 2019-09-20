from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.
def test_ListaClientes_is_resolved(self):
    url = reverse('cita:ListaClientes')
    self.assertEquals(resolve(url).url_name,'ListaClientes')