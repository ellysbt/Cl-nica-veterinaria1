from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome_equipamento', 'nome_medicamento', 'nome_material']