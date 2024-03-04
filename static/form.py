from django import forms
from app_listaDeTarefas.models import ListadeTareda

class ListadeTarefaForm(forms.ModelForm):
    class Meta:
        model = ListadeTareda
        fields = '__all__'