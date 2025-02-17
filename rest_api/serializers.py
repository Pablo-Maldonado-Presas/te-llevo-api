from rest_framework import serializers
from core.models import Usuario, Viaje

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['rut', 'correo', 'contrasennia', 'nombre', 'apellidoPaterno', 'apellidoMaterno', 'carrera', 'sede', 
                  'categoria', 'patenteVehiculo', 'marcaVehiculo', 'modeloVehiculo', 'colorVehiculo']


class ViajeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Viaje
        fields = ['_id', 'sede', 'rut', 'horaSalida', 'capacidadPasajeros', 'precioPorPersona', 'estadoViaje',
                  'patenteVehiculo', 'marcaVehiculo', 'modeloVehiculo', 'colorVehiculo', 'correoChofer', 'correoPasajero']