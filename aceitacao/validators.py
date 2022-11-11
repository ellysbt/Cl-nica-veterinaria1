from django.core.exceptions import ValidationError
import datetime

def teste_nome(value):
    if len(value) < 3:
        raise ValidationError('O nome tem que possuir no mínimo 3 caracteres!')
    else:
        return value

def teste_cpf(value):
    if len(str(value)) != 11:
        raise ValidationError('O campo cpf tem que ter 11 digitos!')
    else:
        return value

def teste_rg(value):
    if len(str(value)) != 7:
        raise ValidationError('O campo rg tem que ter 7 digitos!')
    else:
        return value

def teste_telefone(value):
    if len(str(value)) != 11:
        raise ValidationError('Adicione o DDD!')
    else:
        return value

def teste_email(value):
    if '@' not in value:
        raise ValidationError('Está faltando o "@"')
    else:
        return value

def teste_sem_numero(value):
    if any(n.isdigit() for n in value):
        raise ValidationError('Não pode ter números, apenas letras!')
    else:
        return value

def teste_data(value):
    user = value
    server = datetime.datetime.today()
    if str(user) > str(server):
        raise ValidationError('Data inválida')
    else:
        return value