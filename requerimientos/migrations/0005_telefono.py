# Generated by Django 4.1.1 on 2022-09-21 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0004_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono1', models.IntegerField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimientos.usuario')),
            ],
            options={
                'db_table': 'telefono',
            },
        ),
    ]
