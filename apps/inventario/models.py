from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
	referencia =  models.CharField(max_length=50, blank=False, null=False, unique=True)
	marca = models.CharField(max_length=50, blank=False, null=False)
	procesador = models.CharField(max_length=50, blank=False, null=False)
	memoria = models.CharField(max_length=50, blank=False, null=False)
	disco = models.CharField(max_length=50, blank=False, null=False)
	tipo = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return str(self.referencia)

	class Meta:
		verbose_name = "Equipo"
		verbose_name_plural = "Equipos"

class EquipoUsuario(models.Model):
	equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE, null=False, blank=False)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	fecha_de_asignacion = models.DateField(auto_now_add=False, null=False, blank=False)
	fecha_de_entrega = models.DateField(auto_now_add=False, null=False, blank=False)

	def __str__(self):
		return str(self.id)