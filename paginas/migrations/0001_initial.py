# Generated by Django 4.1 on 2022-09-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gmp',
            fields=[
                ('patri', models.IntegerField(primary_key=True, serialize=False, verbose_name='patrimonio')),
                ('serie', models.CharField(max_length=60, verbose_name='Nº de Série')),
                ('produto', models.CharField(max_length=100, verbose_name='Produto')),
                ('escola', models.CharField(max_length=200, verbose_name='Escola')),
                ('funci', models.CharField(max_length=200, verbose_name='Funcionário')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Entregue em ')),
            ],
        ),
    ]
