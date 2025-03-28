from django.db import models
from django.forms import CharField


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id}) {self.descricao.upper()}"
