from django.db import models
from aceitacao.validators import teste_nome, teste_sem_numero, teste_data

class Animal(models.Model):
    nome_pet = models.CharField(max_length=256, validators=[teste_nome, teste_sem_numero])
    data_de_nascimento_pet = models.DateField(validators=[teste_data])
    especie_pet = models.CharField(max_length=20, validators=[teste_sem_numero])
    raca_pet = models.CharField(max_length=20, validators=[teste_sem_numero])

    def __str__(self) -> str:
        return self.nome_pet