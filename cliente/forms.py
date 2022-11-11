from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    data_nascimento_cli = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Cliente
        fields = ['nome_completo_cli', 'data_nascimento_cli', 'cpf_cli', 'rg_cli', 'telefone_cli', 'email_cli']