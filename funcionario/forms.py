from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    data_nascimento_func = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Funcionario
        fields = ['nome_completo_func', 'data_nascimento_func', 'cpf_func', 'rg_func', 'telefone_func', 'email_func']