import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .forms import TarefaForm
from .models import TarefaModel



def tarefas_home(request):
    tarefas = TarefaModel.objects.select_related("categoria").all()
    total      = tarefas.count()
    concluidas = tarefas.filter(completo=True).count()
    pendentes  = total - concluidas
    urgentes   = tarefas.filter(prioridade="urgente", completo=False).count()

    contexto = {
        "nome": "Lucas",
        "tarefas": tarefas,
        "total": total,
        "concluidas": concluidas,
        "pendentes": pendentes,
        "urgentes": urgentes,
        
        "chart_labels": json.dumps(["Concluídas", "Pendentes"]),
        "chart_data":   json.dumps([concluidas, pendentes]),
       
        "stats": [
            ("Total",      total,      "list-todo",      "bg-indigo-500/20 text-indigo-400"),
            ("Concluídas", concluidas, "check-circle-2", "bg-green-500/20  text-green-400"),
            ("Pendentes",  pendentes,  "clock",          "bg-amber-500/20  text-amber-400"),
            ("Urgentes",   urgentes,   "flame",          "bg-red-500/20    text-red-400"),
        ],
    }
    return render(request, "tarefas/home.html", contexto)



def tarefas_kanban(request):
   
    colunas = [
        (key, label, list(TarefaModel.objects.filter(status=key).order_by("ordem")))
        for key, label in TarefaModel.Status.choices
    ]
    return render(request, "tarefas/kanban.html", {"colunas": colunas})



def tarefas_adicionar(request):
    form = TarefaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        if request.headers.get("HX-Request"):          
            return HttpResponse(
                '<div class="toast" x-data x-init="setTimeout(()=>$el.remove(),3000)">'
                '✅ Tarefa criada com sucesso!</div>'
            )
        return redirect("tarefas:home")
    return render(request, "tarefas/adicionar.html", {"form": form})


def tarefas_editar(request, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    form   = TarefaForm(request.POST or None, instance=tarefa)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tarefas:home")
    return render(request, "tarefas/editar.html", {"form": form, "tarefa": tarefa})


def tarefas_remover(request, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method in ("POST", "DELETE"):
        tarefa.delete()
        if request.headers.get("HX-Request"):
            return HttpResponse("")
        return redirect("tarefas:home")
    return redirect("tarefas:home")



@require_POST
def tarefas_toggle(request, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.completo = not tarefa.completo
    tarefa.save(update_fields=["completo"])
    if request.headers.get("HX-Request"):
        return render(request, "tarefas/_status_badge.html", {"tarefa": tarefa})
    return JsonResponse({"completo": tarefa.completo})



@csrf_exempt
@require_POST
def tarefas_reordenar(request):  
    data = json.loads(request.body)
    for item in data:
        TarefaModel.objects.filter(id=item["id"]).update(
            status=item["status"],
            ordem=item["ordem"],
        )
    return JsonResponse({"ok": True})