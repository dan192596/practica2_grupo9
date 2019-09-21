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

    #USO PARA ADMINISTRADOR
    url(r'^administrador$',views.homeAdmin,name='home_admin'),
    url(r'^administrador/nuevo_usuario$', views.createUser, name='create_user'),
    url(r'^administrador/actualizar_usuario',views.updateUser,name='update_user'),
    url(r'^administrador/eliminar_usuario',views.deleteUser,name='delete_user'),
]