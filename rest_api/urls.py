from django.urls import path
from rest_api.views import lista_usuarios, lista_viajes
 
from . import views

urlpatterns=[
    path('lista_usuarios', lista_usuarios, name="Lista Usuarios"),
    path('lista_viajes', lista_viajes, name="Lista Viajes"),
    path('lista_viajes/<str:_id>', lista_viajes, name="Detalle Viaje"),
]