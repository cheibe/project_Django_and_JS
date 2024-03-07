from django.contrib import admin
from .models import ListadeTareda

class ListaAdmin(admin.ModelAdmin):
    list_display = ('id','tarefa', 'status')

admin.site.register(ListadeTareda, ListaAdmin)
