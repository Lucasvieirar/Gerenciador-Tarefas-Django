from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns =[
    path("", views.tarefas_home, name="home"),
    path("adicionar/", views.tarefas_adicionar, name="adicionar" )

]