# Generated by Django 5.1.2 on 2024-11-07 08:52

import faculdade.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, validators=[faculdade.models.nome_existe])),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, validators=[faculdade.models.nome_existe])),
                ('descricao', models.TextField()),
                ('alunos', models.ManyToManyField(related_name='cursos', to='faculdade.aluno')),
            ],
        ),
    ]