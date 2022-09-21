# Generated by Django 4.1.1 on 2022-09-21 11:56

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0005_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frente_numero', models.IntegerField()),
                ('block_casa_dpto', models.CharField(max_length=6)),
                ('lista_calles_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimientos.listacalles')),
            ],
            options={
                'verbose_name': 'Incidente',
                'verbose_name_plural': 'Incidentes',
                'db_table': 'incidente',
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Imagenincidentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='incidentes')),
                ('descripcion_fotografia', models.CharField(max_length=100)),
                ('incidente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimientos.incidente')),
            ],
            options={
                'verbose_name': 'Imagen Incidente',
                'verbose_name_plural': 'Imagenes Incidentes',
                'db_table': 'imagenincidentes',
                'ordering': ['incidente_id'],
            },
        ),
    ]
