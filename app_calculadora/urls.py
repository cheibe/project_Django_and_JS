from django.urls import path
from app_calculadora import views

urlpatterns = [
    path('', views.calculadora_view, name='calculadora')
]
