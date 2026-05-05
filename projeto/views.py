from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Rota de teste")

def index_view(resquest):
    return HttpResponse("Bem vindo")