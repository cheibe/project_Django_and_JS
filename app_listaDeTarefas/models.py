from django.db import models

STATUS = [
    ('fazer', 'A fazer'),
    ('concluido', 'Concluido')
]

class ListadeTareda(models.Model):
    tarefa = models.CharField(max_length=255, verbose_name='Tarefa')
    status = models.CharField(max_length=30, choices=STATUS, default='fazer')

    def __str__(self):
        return self.tarefa