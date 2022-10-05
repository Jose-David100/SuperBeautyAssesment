from django.contrib import admin
from apps.inventario.models import Equipo, EquipoUsuario

# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
	list_display = ('id', 'referencia', 'marca', 'tipo')
	list_display_links = ('referencia',)
	list_filter = ('tipo', )
	search_fields = ('referencia',)

class EquipoUsuarioAdmin(admin.ModelAdmin):
	list_display = ('id', 'equipo', 'usuario', 'fecha_de_asignacion')
	list_display_links = ('equipo',)
	list_filter = ('fecha_de_asignacion', 'usuario' )


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(EquipoUsuario, EquipoUsuarioAdmin)