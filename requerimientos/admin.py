from django.contrib import admin

# Register your models here.

from .models import *


admin.site.site_header = "App Ventanilla Web"
admin.site.site_title = "Portal de Administración Ventanilla Requerimientos"
admin.site.index_title = "Bienvenidos al portal de administración Ventanilla Web"


admin.site.register(Agrupacion)
admin.site.register(Categoria)
admin.site.register(Detalleagrupacion)
admin.site.register(Detallecategoria)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Estadocivil)
admin.site.register(Genero)
admin.site.register(Listacalles)
admin.site.register(Motivo)
admin.site.register(Nacionalidad)
admin.site.register(Prioridad)
admin.site.register(Redessociales)
admin.site.register(Tiposolicitante)
admin.site.register(Unidadvecinal)
admin.site.register(Departamento)
admin.site.register(Origen)
admin.site.register(Telefono)
admin.site.register(Usuario)
admin.site.register(Incidente)
admin.site.register(Imagenincidentes)
admin.site.register(Requerimientos)
admin.site.register(Cambiosestado)
admin.site.register(Domicilio)








