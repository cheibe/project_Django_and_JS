from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', context={
        'home': home,
    })