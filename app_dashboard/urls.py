from django.urls import path
from app_dashboard import views


urlpatterns = [
    path('', views.home_view, name='home')
]
