# Generated by Django 4.1.1 on 2022-09-22 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0015_imagenincidentes_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='digito_verif',
            field=models.CharField(help_text='Digito verificador del rut', max_length=2),
        ),
    ]
