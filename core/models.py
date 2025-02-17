from django.db import models
from bson import ObjectId

def get_objectid():
    return str(ObjectId())

# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, unique=True, max_length=10, verbose_name="Rut de Usuario") # Rut sin puntos y con guión
    correo = models.CharField(max_length=100, unique=True, verbose_name="Correo de Usuario")
    contrasennia = models.CharField(max_length=20, verbose_name="Contrasennia de Usuario")
    nombre = models.CharField(max_length=50, verbose_name="Primer nombre de Usuario")
    apellidoPaterno = models.CharField(max_length=50, verbose_name="Apellido paterno de Usuario")
    apellidoMaterno = models.CharField(max_length=50, verbose_name="Apellido materno de Usuario")
    carrera = models.CharField(max_length=100, verbose_name="Carrera de Usuario")
    sede = models.CharField(max_length=50, verbose_name="Sede de Usuario")
    
    categoria = models.CharField(max_length=50, verbose_name = "Nombre de Categoria de Usuario")
    patenteVehiculo = models.CharField(max_length=10, blank=True, verbose_name="Patente del Vehículo de Usuario Chofer")
    marcaVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Marca del Vehículo")
    modeloVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Modelo del Vehículo")
    colorVehiculo = models.CharField(max_length=20, blank=True, verbose_name="Color del Vehículo")


    def __str__(self):
        texto = "({0}) {1} {2} {3}"
        return texto.format(self.rut, self.categoria, self.nombre, self.apellidoPaterno)
    

class Viaje(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=get_objectid, editable=False)
    sede = models.CharField(max_length=30, verbose_name="Sede Duoc")
    rut = models.CharField(unique=True, max_length=10, verbose_name="Rut de Usuario Chofer")
    horaSalida = models.CharField(max_length=20, verbose_name="Hora de salida")
    capacidadPasajeros = models.IntegerField(default=1, verbose_name="Capacidad de pasajeros")
    precioPorPersona = models.IntegerField(verbose_name="Precio por Persona")
    estadoViaje = models.CharField(max_length=20, verbose_name="Estado del viaje") # Programado, En curso, Completado, Cancelado

    patenteVehiculo = models.CharField(max_length=10, blank=True, verbose_name="Patente del Vehículo de Usuario Chofer")
    marcaVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Marca del Vehículo")
    modeloVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Modelo del Vehículo")
    colorVehiculo = models.CharField(max_length=20, blank=True, verbose_name="Color del Vehículo")

    correoChofer = models.CharField(max_length=50, verbose_name="Correo de Usuario Chofer")
    correoPasajero = models.TextField(default='', blank=True, verbose_name="Correos de los Pasajeros")

    def get_correoPasajero(self):
        return self.correoPasajero.split(',')

def set_correoPasajero(self, correos_list):
    if correos_list:
        self.correoPasajero = ','.join(correos_list)
    else:
        self.correoPasajero = ' '

    
    def __str__(self):
        texto = "({0}) {1}"
        return texto.format(self.patenteVehiculo, self.estadoViaje)



