from django.db import models

class ListadeTareda(models.Model):
    tarefa = models.CharField(max_length=255, verbose_name='Tarefa')

    def __str__(self):
        return self.tarefa