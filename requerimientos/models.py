
from django.db import models

# Create your models here.


class Agrupacion(models.Model):
    agrupacion = models.CharField(max_length=100)

    def __str__(self):
        return self.agrupacion
    
    class Meta:
        db_table = 'agrupacion'
        verbose_name_plural = "Agrupaciones"
        verbose_name = "Agrupacion"
        ordering = ['agrupacion']

class Categoria(models.Model):
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.categoria

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"
        ordering = ['categoria']

class Detalleagrupacion(models.Model):
    detalle = models.CharField(max_length=100)

    def __str__(self):
        return self.detalle

    class Meta:
        db_table = 'detalleagrupacion'

class Detallecategoria(models.Model):
    detalle = models.CharField(max_length=150)

    def __str__(self):
        return self.detalle

    class Meta:
        db_table = 'detallecategoria'

class Direccion(models.Model):
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.direccion

    class Meta:
        db_table = 'direccion'

class Estado(models.Model):
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado

    class Meta:
        db_table = 'estado'

class Estadocivil(models.Model):
    estado_civil = models.CharField(max_length=100)

    def __str__(self):
        return self.estado_civil

    class Meta:
        db_table = 'estadocivil'

class Genero(models.Model):
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

    class Meta:
        db_table = 'genero'

class Listacalles(models.Model):
    calle = models.CharField(max_length=200)

    def __str__(self):
        return self.calle

    class Meta:
        db_table = 'listacalles'

class Motivo(models.Model):
    motivo = models.CharField(max_length=80)

    def __str__(self):
        return self.motivo

    class Meta:
        db_table = 'motivo'

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nacionalidad

    class Meta:
        db_table = 'nacionalidad'

class Prioridad(models.Model):
    prioridad = models.CharField(max_length=100)
    cantidad_de_dias = models.IntegerField()

    def __str__(self):
        return self.prioridad

    class Meta:
        db_table = 'prioridad'

class Redessociales(models.Model):
    red_social = models.CharField(max_length=80)

    def __str__(self):
        return self.red_social

    class Meta:
        db_table = 'redessociales'

class Tiposolicitante(models.Model):
    tipo_solicitante = models.CharField(max_length=80)

    def __str__(self):
        return self.tipo_solicitante

    class Meta:
        db_table = 'tiposolicitante'

class Unidadvecinal(models.Model):
    unidad_vecinal = models.CharField(max_length=100)

    def __str__(self):
        return self.unidad_vecinal

    class Meta:
        db_table = 'unidadvecinal'

class Departamento(models.Model):
    departamento = models.CharField(max_length=100)
    id_direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)

    def __str__(self):
        return self.departamento

    class Meta:
        db_table = 'departamento'

class Origen(models.Model):
    tipo = models.CharField(max_length=80)
    rrss_id = models.ForeignKey('Redessociales', on_delete=models.CASCADE)
    datos_persona = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


    class Meta:
        db_table = 'origen'

class Telefono(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    telefono1 = models.IntegerField()

    def __str__(self):  
        return self.telefono1

    class Meta:
        db_table = 'telefono'

class Usuario(models.Model):
    rut = models.IntegerField()
    digito_verif = models.CharField(max_length=2)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100)
    apellido_pat = models.CharField(max_length=100)
    apellido_mat = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    id_estado_civil = models.ForeignKey(Estadocivil, on_delete=models.CASCADE)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    correo = models.EmailField()

    def __str__(self):
        return self.rut+"-"+self.digito_verif

    class Meta:
        db_table = 'usuario'
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"
        ordering = ['rut']

class Incidente(models.Model):
    lista_calles_id = models.ForeignKey(Listacalles, on_delete=models.CASCADE)
    frente_numero = models.IntegerField()
    block_casa_dpto = models.CharField(max_length=6)
  

    class Meta:
        db_table = 'incidente'
        verbose_name_plural = "Incidentes"
        verbose_name = "Incidente"
        ordering = [id]

class Imagenincidentes(models.Model):
    incidente_id = models.ForeignKey('Incidente', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='incidentes')
    descripcion_fotografia = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion_fotografia
 
    class Meta:
        db_table = 'imagenincidentes'
        verbose_name_plural = "Imagenes Incidentes"
        verbose_name = "Imagen Incidente"
        ordering = ['incidente_id']

class Requerimientos(models.Model):
    id_origen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    id_prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    id_motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField()
    fecha_cierre_estimado = models.DateField()
    respuesta = models.CharField(max_length=300)
    motivo_negativa = models.CharField(max_length=200)
    id_tiposolicitante = models.ForeignKey(Tiposolicitante, on_delete=models.CASCADE)
    id_incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_Motivo


    class Meta:
        db_table = 'requerimientos'
        verbose_name_plural = "Requerimientos"
        verbose_name = "Requerimiento"

class Cambiosestado(models.Model):
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora_cambioestado = models.DateTimeField() 
    dato_cambiado = models.CharField(max_length=500, help_text='Dato que se modificó')  

    def __str__(self):
        return self.id_estado
   
    class Meta:
        db_table = 'cambiosestado'
        verbose_name = 'Cambio de estado'
        verbose_name_plural = 'Cambios de estado'

class Domicilio(models.Model):
    id_calle = models.ForeignKey(Listacalles, on_delete=models.CASCADE)
    numero = models.IntegerField()
    casa_dpto = models.CharField(max_length=6)
    id_unidad_vecinal = models.ForeignKey(Unidadvecinal, on_delete=models.CASCADE)
    id_agrupacion = models.ForeignKey(Agrupacion, on_delete=models.CASCADE)
    id_detalle_agrupacion = models.ForeignKey(Detalleagrupacion, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domicilio'
        verbose_name_plural = "Domicilios"
        verbose_name = "Domicilio"
