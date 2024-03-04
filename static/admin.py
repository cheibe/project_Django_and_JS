from django.contrib import admin
from .models import ListadeTareda

class ListaAdmin(admin.ModelAdmin):
    ...

admin.site.register(ListadeTareda, ListaAdmin)
