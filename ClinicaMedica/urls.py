from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'CM'
urlpatterns = [
    url(r'^$', views.indexL, name='index'),
    url(r'^perfil/$', views.profile, name='perfil'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^ListaClientes/$', views.ListaClientes, name='ListaClientes'),
    url(r'^Cliente/(?P<codigo>.+)$', views.InfoCliente, name='InfoCliente'),
]