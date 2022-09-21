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

#------------------------------------------------------------

class Estado(models.Model):
    estado = models.CharField(max_length=100)

    class Meta:
        db_table = 'estado'


class Estadocivil(models.Model):
    estado_civil = models.CharField(max_length=100)

    class Meta:
        db_table = 'estadocivil'


class Genero(models.Model):
    genero = models.CharField(max_length=100)

    class Meta:
        db_table = 'genero'


