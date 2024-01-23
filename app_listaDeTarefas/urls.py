from django.urls import path
from app_listaDeTarefas import views

urlpatterns = [
    path('lista_de_tarefas/', views.lista_tarefa_view, name='lista_tarefas')
]
