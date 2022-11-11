from django.db import models
from django.forms import DateField
from aceitacao.validators import teste_nome, teste_cpf, teste_rg, teste_telefone, teste_email, teste_sem_numero, teste_data

class Funcionario(models.Model):
    nome_completo_func = models.CharField(max_length=256, validators=[teste_nome, teste_sem_numero])
    data_nascimento_func = models.DateField(validators=[teste_data])
    cpf_func = models.IntegerField(unique=True, validators=[teste_cpf])
    rg_func = models.IntegerField(unique=True, validators=[teste_rg])
    telefone_func = models.CharField(unique=True, max_length=256, validators=[teste_telefone])
    email_func = models.CharField(unique=True, max_length=256, validators=[teste_email])

    def __str__(self) -> str:
        return self.nome_completo_func