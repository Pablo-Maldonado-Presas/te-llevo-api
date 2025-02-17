from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario, Viaje
from .serializers import UsuarioSerializer, ViajeSerializer


# Create your views here.
@csrf_exempt

@api_view(['GET'])
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def lista_viajes(request, _id=None):
    if request.method == 'GET':
        if _id is not None:
            viaje = Viaje.objects.get(_id=_id)
            serializer = ViajeSerializer(viaje)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            viajes = Viaje.objects.all()
            serializer = ViajeSerializer(viajes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ViajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        viaje = Viaje.objects.get(_id=_id)
        serializer = ViajeSerializer(viaje, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        viaje = Viaje.objects.get(_id=_id)
        viaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



