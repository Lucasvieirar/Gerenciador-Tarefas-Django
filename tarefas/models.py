# from django.db import models


# class TarefaModel(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.TextField(null=True, blank=True)
#     completo = models.BooleanField(default=False)
#     data_criacao = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.nome

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50),
    cor = models.CharField(max_length=7, default="#6366f1") 

    def __set__(self):
        
        return self.nome

class TarefaModel(models.Model):

    class Prioridade(models.TextChoices):
        BAIXA  = "baixa",  "Baixa"
        MEDIA  = "media",  "Média"
        ALTA   = "alta",   "Alta"
        URGENTE = "urgente", "Urgente"

    class Status(models.TextChoices):
        BACKLOG     = "backlog",     "Backlog"
        A_FAZER     = "a_fazer",     "A Fazer"
        EM_PROGRESSO = "em_progresso", "Em Progresso"
        CONCLUIDO   = "concluido",   "Concluído"
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField(nul=True, blank=True)
    completo = models.BooleanField(default=False)
    Prioridade = models.CharField(
        max_length=10,
        choices=Prioridade.choices,
        default=Prioridade.MEDIA,
    )
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.A_FAZER,
    )
    Categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        null= True, blank=True,
        related_name="tarefas",
    )
    prazo = models.DateField(null=True, blank=True)
    ordem = models.PositiveIntegerField(default=0)
    data_criacao = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
class Meta:
    ordering = ["ordem", "-data_criacao"]

def __str__(self):
    return self.nome
