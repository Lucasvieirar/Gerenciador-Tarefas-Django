from django.db import models


class TarefaModel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome