from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Clinica'
urlpatterns = [
    url(r'^$',views.index, name='index'),
]