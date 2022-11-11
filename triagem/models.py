from django.db import models
from animal.models import Animal

class Triagem(models.Model):
    nome_do_pet = models.ForeignKey(Animal, on_delete=models.CASCADE)
    sintomas = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.nome_do_pet