from django.db import models

from click.core import V 

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} ({self.id})'
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'