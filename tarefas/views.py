from django.shortcuts import render

from django.http import HttpResponse

def tarefas_home(request):
    contexto = {
        "nome": "Lucas"
    }
    return  render(request,'tarefas/home.html', contexto)

def tarefas_adicionar(request):
    return HttpResponse("adcione sua tarefas")
    
