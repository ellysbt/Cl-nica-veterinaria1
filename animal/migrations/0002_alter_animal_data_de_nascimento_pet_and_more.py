# Generated by Django 4.1.2 on 2022-11-09 18:52

import aceitacao.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='data_de_nascimento_pet',
            field=models.DateField(validators=[aceitacao.validators.teste_data]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='especie_pet',
            field=models.CharField(max_length=20, validators=[aceitacao.validators.teste_sem_numero]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='nome_pet',
            field=models.CharField(max_length=256, validators=[aceitacao.validators.teste_nome, aceitacao.validators.teste_sem_numero]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='raca_pet',
            field=models.CharField(max_length=20, validators=[aceitacao.validators.teste_sem_numero]),
        ),
    ]
