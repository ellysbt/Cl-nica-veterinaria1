from django.db import models
from django.forms import DateField
from aceitacao.validators import teste_nome

class Equipamento(models.Model):
    nome_equipamento = models.CharField(max_length=256, validators=[teste_nome])
    nome_medicamento = models.CharField(max_length=256, validators=[teste_nome])
    nome_material = models.CharField(max_length=256, validators=[teste_nome])

    def __str__(self) -> str:
        return self.nome_equipamento