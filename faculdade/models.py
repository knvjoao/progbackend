from django.db import models
from django.core.exceptions import ValidationError
import re


#função para validar o nome, serve para curso e aluno. não foi 100% testada, só para invalidar os casos mais claros. usando regular expressions.
def nome_existe(nome):
    nome = nome.lower()
    for char in nome:
        if not re.match(r'[a-zà-ýÿ\s]', char):
            raise ValidationError('Nome inválido. Digitou algum caractere errado?')
        
#classe aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=200, validators=[nome_existe])
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
#classe curso
class Curso(models.Model):
    titulo = models.CharField(max_length=100, validators=[nome_existe])
    descricao = models.TextField()
    alunos = models.ManyToManyField(Aluno, related_name="cursos")

    def __str__(self):
        return self.titulo