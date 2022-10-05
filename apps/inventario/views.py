# IMPORTACIONES DJANGO-REST-FRAMEWORK
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# IMPORTACION DEL MODEL EQUIPO
from apps.inventario.models import Equipo

# .6 CREAR APIVIEW CON EL METODO GET PARA CONSULTAR LA LISTA DE EQUIPOS

# Serializacion del model
class EquiposSerializers(serializers.ModelSerializer):
	class Meta:
		model = Equipo
		fields = '__all__'


# VISTA DE LA API

# Listado de Equipos
class ListadoEquipos(APIView):
	def get(self, request):
		equipo = Equipo.objects.all()
		data = EquiposSerializers(equipo, many=True).data
		return Response(data)

# EXTRA: Detalle del Equipo (Busqueda por REFERENCIA)

class DetalleEquipos(APIView):
	def get(self, request, referencia):
		equipo = get_object_or_404(Equipo, referencia= referencia )
		data = EquiposSerializers(equipo).data
		return Response(data)