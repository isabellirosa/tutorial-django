from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)


    def __str__(self):
        return f'{self.nome} ({self.id}) quantidade:{self.quantidade}'