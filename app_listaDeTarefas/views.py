from django.shortcuts import render, redirect, get_object_or_404
from app_listaDeTarefas.models import ListadeTareda
from app_listaDeTarefas.form import ListadeTarefaForm, EditListadeTarefaForm

def lista_tarefa_view(request):
    if request.method == 'POST':
        form = ListadeTarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaDeTarefa:lista_tarefas')
    else:
        form = ListadeTarefaForm()
    
    tarefas = ListadeTareda.objects.all()
    return render(request, 'pages/home_lista.html', context={
        'lista_tarefa': lista_tarefa_view,
        'form': form,
        'tarefas': tarefas
    })

def delete_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(ListadeTareda, pk=tarefa_id)
    
    if request.method == 'POST':
        tarefa.delete()
        tarefas = ListadeTareda.objects.all()
        return redirect('ListaDeTarefa:lista_tarefas')

    return render(request, 'pages/home_lista.html', context={
        'lista_tarefa': lista_tarefa_view,
        'tarefas': tarefas
    })

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(ListadeTareda, pk=tarefa_id)
    if request.method == 'POST':
        form = EditListadeTarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('ListaDeTarefa:lista_tarefas')
        else:
            form = EditListadeTarefaForm(instance=tarefa)
        
        return render(request, "ListaDeTarefa:editar_lista", context={
            'form': form,
        })