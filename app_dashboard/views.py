from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html', context={
        'home': home_view,
    })