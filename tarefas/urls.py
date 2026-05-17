# from django.urls import path
# from . import views

# app_name = "tarefas"

# urlpatterns =[
#     path("", views.tarefas_home, name="home"),
#     path("adicionar/", views.tarefas_adicionar, name="adicionar" ),
#     path("remover/<int:id>", views.tarefas_remover, name="remover"),
#     path("editar/<int:id>", views.tarefas_editar, name='editar')


# ]

from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path("",                        views.tarefas_home,      name="home"),
    path("kanban/",                 views.tarefas_kanban,    name="kanban"),
    path("adicionar/",              views.tarefas_adicionar, name="adicionar"),
    path("editar/<int:id>/",        views.tarefas_editar,    name="editar"),
    path("remover/<int:id>/",       views.tarefas_remover,   name="remover"),
    path("toggle/<int:id>/",        views.tarefas_toggle,    name="toggle"),
    path("reordenar/",              views.tarefas_reordenar, name="reordenar"),
]