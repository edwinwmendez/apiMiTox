# Generated by Django 4.0.4 on 2022-11-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiAuth', '0003_alter_autorizacion_codigo_auth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='codigo_auth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiAuth.codigoauth'),
        ),
    ]