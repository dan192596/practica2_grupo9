from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.
def test_ListaClientes_is_resolved(self):
    url = reverse('CM:ListaClientes')
    self.assertEquals(resolve(url).url_name,'ListaClientes')

def test_InformacionCliente_is_resolved(self):
    url = reverse('CM:InfoCliente')
    self.assertEquals(resolve(url).url_name,'InfoCliente')