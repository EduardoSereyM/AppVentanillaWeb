# Generated by Django 4.1.1 on 2022-09-21 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimientos.direccion')),
            ],
            options={
                'db_table': 'departamento',
            },
        ),
    ]