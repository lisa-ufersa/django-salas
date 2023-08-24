from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sala(models.Model):
    nome = models.CharField(max_length=150)
    local = models.CharField(max_length=150)
    capacidade = models.IntegerField()
    is_lab = models.BooleanField()

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.local
    
class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    descricao = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.local
