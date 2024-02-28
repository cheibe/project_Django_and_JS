from django.urls import path
from app_listaDeTarefas import views

urlpatterns = [
    path('', views.lista_tarefa_view, name='lista_tarefas')
]
