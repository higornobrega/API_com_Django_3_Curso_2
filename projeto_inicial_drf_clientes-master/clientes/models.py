from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    mensagem = models.TextField('Mensagem')

    def __str__(self):
        return self.nome
