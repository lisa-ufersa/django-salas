from django.db import models

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