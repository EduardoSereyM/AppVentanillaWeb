# Generated by Django 4.1.1 on 2022-09-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0007_requerimientos_domicilio_cambiosestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='prioridad',
            name='cantidad_de_dias',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
