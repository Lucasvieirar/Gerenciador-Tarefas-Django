from django.shortcuts import render

from django.http import HttpResponse

def tarefas_home(request):
    return HttpResponse("Aqui estão suas tarefas")

def tarefas_adicionar(request):
    return HttpResponse("adcione sua tarefas")
    
