# Generated by Django 4.1 on 2022-12-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios_sistema',
            fields=[
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=80)),
                ('user', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=64)),
                ('nivel', models.CharField(max_length=15)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
