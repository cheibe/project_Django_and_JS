from django.urls import path
from app_listaDeTarefas import views

app_name = 'ListaDeTarefa'

urlpatterns = [
    path('', views.lista_tarefa_view, name='lista_tarefas'),
    path('delete/<tarefa_id>', views.delete_tarefa, name='delete_tarefa'),
    path('editar/<tarefa_id>', views.editar_tarefa, name='editar_lista'),
]
