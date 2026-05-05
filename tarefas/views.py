from django.shortcuts import render

from .forms import  TarefaForm

def tarefas_home(request):
    contexto = {
        "nome": "Lucas"
    }
    return  render(request,'tarefas/home.html', contexto)

def tarefas_adicionar(request):
    contexto = {
        "form": TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)
    
