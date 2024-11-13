from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    validade = models.DateField()

    def __str__(self):
        return self.nome