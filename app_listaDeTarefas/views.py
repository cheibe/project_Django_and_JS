from django.shortcuts import render

def lista_tarefa_view(request):
    return render(request, 'pages/home_lista.html', context={
        'lista_tarefa': lista_tarefa_view,
    })