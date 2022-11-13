# Generated by Django 4.0.4 on 2022-11-12 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('codigo_auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiAuth.autorizacion')),
            ],
        ),
    ]