# Generated by Django 4.2 on 2024-12-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiAppMedicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicomodels',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='medicomodels',
            name='matricula',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='medicomodels',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='medicomodels',
            name='profesion',
            field=models.CharField(max_length=30),
        ),
    ]
