# Generated by Django 4.0.4 on 2022-11-13 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=50)),
                ('usuario', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CodigoAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_auth', models.CharField(blank=True, max_length=25, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiAuth.usuario')),
            ],
        ),
    ]
