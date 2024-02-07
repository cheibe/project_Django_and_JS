from django.shortcuts import render

def calculadora_view(request):
    return render(request, 'pages/home_calculadora.html', context={
        'calculadora': calculadora_view,
    })
