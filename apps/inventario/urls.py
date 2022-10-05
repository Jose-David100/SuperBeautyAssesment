from django.urls import path
from apps.inventario.views import ListadoEquipos, DetalleEquipos

app_name = 'inventario'

urlpatterns = [
	path('api/equipo/', ListadoEquipos.as_view(), name="equipo_view"),
	path('api/equipo/<str:referencia>', DetalleEquipos.as_view(), name="detalle_equipo"),
]