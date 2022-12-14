# Generated by Django 4.1.2 on 2022-10-26 19:13

import aceitacao.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_equipamento', models.CharField(max_length=256, validators=[aceitacao.validators.teste_nome])),
                ('nome_medicamento', models.CharField(max_length=256, validators=[aceitacao.validators.teste_nome])),
                ('nome_material', models.CharField(max_length=256, validators=[aceitacao.validators.teste_nome])),
            ],
        ),
    ]
